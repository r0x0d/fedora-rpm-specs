Name:           virtme-ng
Version:        1.30
Release:        %autorelease
Summary:        Quickly build and run kernels inside a virtualized snapshot of your live system

License:        GPL-2.0-only
URL:            https://github.com/arighi/%{name}
Source:         %{pypi_source %{name}}

BuildArch:      noarch

BuildRequires:  python3-devel

Recommends:     qemu-kvm
Recommends:     busybox
Recommends:     virtiofsd >= 1.7.0

# virtme-ng provides a mostly compatible CLI w.r.t. the original virtme,
# which is dead upstream, so obsolete it in favor of the new package.
Obsoletes:      virtme < 0.1.1-25
Provides:       virtme = %{version}-%{release}

%description
virtme-ng is a tool that allows to easily and quickly recompile and test a Linux
kernel, starting from the source code.

It allows to recompile the kernel in few minutes (rather than hours), then the
kernel is automatically started in a virtualized environment that is an exact
copy-on-write copy of your live system, which means that any changes made to the
virtualized environment do not affect the host system.

In order to do this a minimal config is produced (with the bare minimum support
to test the kernel inside qemu), then the selected kernel is automatically built
and started inside qemu, using the filesystem of the host as a copy-on-write
snapshot.

This means that you can safely destroy the entire filesystem, crash the kernel,
etc. without affecting the host.

Kernels produced with virtme-ng are lacking lots of features, in order to reduce
the build time to the minimum and still provide you a usable kernel capable of
running your tests and experiments.

virtme-ng is based on virtme, written by Andy Lutomirski <luto@kernel.org>.

%prep
%autosetup -p1 -n %{name}-%{version}

# Remove bundled binary (optional optimized init program for the VM)
rm -f virtme/guest/bin/virtme-ng-init

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files virtme virtme_ng

# since version 1.30 we need to install completion scripts manually
function install_completion() {
    local shell="$1"
    local bin="$2"
    local dest="$3"

    register-python-argcomplete -s $shell $bin | \
        install -Dpm 0644 /dev/stdin $RPM_BUILD_ROOT"$dest"
}

function install_completion_bash() {
    local bin="$1"

    install_completion bash "$bin" %{bash_completions_dir}/$bin.bash
}

function install_completion_fish() {
    local bin="$1"

    install_completion fish "$bin" %{fish_completions_dir}/$bin.fish
}

function install_completion_zsh() {
    local bin="$1"

    install_completion zsh "$bin" %{zsh_completions_dir}/_$bin
}

for bin in virtme-ng vng; do
    install_completion_bash $bin
    install_completion_fish $bin
    install_completion_zsh  $bin
done

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/vng
%{_bindir}/virtme-ng
%{_bindir}/virtme-run
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods
%{bash_completions_dir}/{virtme-ng,vng}.bash
%{fish_completions_dir}/{virtme-ng,vng}.fish
%{zsh_completions_dir}/_{virtme-ng,vng}
%{_mandir}/man1/vng.1*

%changelog
%autochangelog
