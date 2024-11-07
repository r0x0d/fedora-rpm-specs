%global     reponame   %{name}.repo
%global     repodir    %{_sysconfdir}/yum.repos.d
%global     thirdparty %{_prefix}/lib/fedora-third-party/conf.d

%define obsoleteLine() %{expand:
Obsoletes: java-%{?1}-openjdk%{?2}%{?3} < 1:100000
Obsoletes: java-%{?1}-openjdk-portable%{?2}%{?3} < 1:1000
}

%define obsoleteLines() %{expand:
%{obsoleteLine -- %{?1} %{?2} %{nil}}
%{obsoleteLine -- %{?1} %{?2} -fastdebug}
%{obsoleteLine -- %{?1} %{?2} -slowdebug}
%{obsoleteLine -- %{?1} %{?2} -unstripped}
}

%define obsoleteJdk() %{expand:
%{obsoleteLines -- %{?1} %{nil}}
%{obsoleteLines -- %{?1} -headless}
%{obsoleteLines -- %{?1} -devel}
%{obsoleteLines -- %{?1} -demo}
%{obsoleteLines -- %{?1} -src}
%{obsoleteLines -- %{?1} -javadoc}
%{obsoleteLines -- %{?1} -javadoc-zip}
%{obsoleteLines -- %{?1} -docs}
%{obsoleteLines -- %{?1} -sources}
}

# 0/1 may vary in time, and is always enabled to 1 per FESCO exception
%global     enabled_by_default 0

Name:       adoptium-temurin-java-repository
Version:    1
Release:    %autorelease
Summary:    Fedora package repository files for yum and dnf along with gpg public keys

License:    EPL-2.0
URL:        https://adoptium.net/installation/linux/#_centosrhelfedora_instructions
Source0:    LICENSE
Source1:    %{name}.conf
Source2:    %{reponame}
Source3:    README.md

BuildArch:  noarch
# fedora-third-party contains tools to work with 3rd party repos and owns fedora-third-party/conf.d/ directory
Requires:   fedora-third-party

#dont forget to update the lua list in post
%{obsoleteJdk -- 1.8.0}
%{obsoleteJdk -- 11}
%{obsoleteJdk -- 17}

%description
This package adds configuration to add a remote repository
of https://adoptium.net/installation/linux/#_centosrhelfedora_instructions ,
if third-party repositories are enabled on a Fedora Linux system.
This repository contains all JDKS which are live and not available in fedora 
as per https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks .
It (4.11.2024) installs: temurin-11-jdk temurin-11-jre temurin-17-jdk temurin-17-jre temurin-21-jdk
 temurin-21-jre temurin-22-jdk temurin-22-jre temurin-23-jdk temurin-23-jre temurin-8-jdk
 temurin-8-jre
Warning, jdk contains both jre and jdk, so if you install jdk and jre (of same version)
you will have two java alternatives masters, and one javac master.
Since f42 it will be obsoleting retired java-(1.8.0,11,17)-openjdk-*

%prep
cat %{SOURCE2} |  sed "s/^enabled=0/enabled=%{enabled_by_default}/" > %{reponame}

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -D -m0644 %{SOURCE1} -t %{buildroot}%{thirdparty}/
install -D -m0644 %{reponame} -t %{buildroot}%{repodir}/
install -D -m0644 %{SOURCE3} -t %{buildroot}%{_docdir}/%{name}/


%pre -p <lua>
local posix = require ("posix")

local jdksKnown={"1.8.0", "11", "17"}
local jdksFound={}
for key, value in pairs(jdksKnown) do
    jdksFound[value]=0;
end
for key, value in pairs(jdksKnown) do
  local java="java-"..value.."-openjdk"
  local jre="jre-"..value.."-openjdk"
  local statJavaJre1 = posix.stat("/usr/lib/jvm/"..java.."/bin/java", "type");
  local statJavaJre2 = posix.stat("/usr/lib/jvm/"..java.."/jre/bin/java", "type");
  local statJavaSdk = posix.stat("/usr/lib/jvm/"..java.."/bin/javac", "type");
  local statJreJre1 = posix.stat("/usr/lib/jvm/"..jre.."/bin/java", "type");
  local statJreJre2 = posix.stat("/usr/lib/jvm/"..jre.."/jre/bin/java", "type");
  local statJreSdk = posix.stat("/usr/lib/jvm/"..jre.."/bin/javac", "type");
  if ((statJavaJre1 ~= nil) or (statJavaJre2 ~= nil) or (statJreJre1 ~= nil) or (statJreJre2 ~= nil)) then
    jdksFound[value]=jdksFound[value]+1;
    if (statJavaSdk ~= nil)or((statJreSdk ~= nil)) then
      jdksFound[value]=jdksFound[value]+1000;
    end
  end
end
for key, value in pairs(jdksFound) do
  temurinKey=key
  if key == "1.8.0" then
    temurinKey=8
  end
  if value > 0 then
    print("You have java-"..key.."-openjdk installed. That is deprecated, and is replaced by temurin-"..temurinKey.."-jre")
  end
  if value > 1000 then
    print("You have java-"..key.."-openjdk-devel installed. That is deprecated, and is replaced by temurin-"..temurinKey.."-jdk")
  end
end



%files
%license LICENSE
%{thirdparty}/*
%config(noreplace) %{repodir}/%{reponame}
%doc README.md

%changelog
%autochangelog
