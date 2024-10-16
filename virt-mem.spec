%define	name	virt-mem
%define	version	0.3.0
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Viewer
License:    GPL
Group:      Graphical desktop/GNOME
URL:        https://et.redhat.com/~rjones/virt-mem/
Source:     http://et.redhat.com/~rjones/virt-mem/files/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  camlp4
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-libvirt-devel
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-bitstring-devel
BuildRequires:  ocaml-gettext-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  perl-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
These are a collection of monitoring and management tools for virtual machines. 

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std \
    OCAML_GETTEXT_EXTRACT_OPTIONS="--extract-default-option '-I +camlp4 pa_o.cmo -I %{ocaml_sitelib}/bitstring bitstring.cma bitstring_persistent.cma pa_bitstring.cmo'" \
    PODIR=%{buildroot}%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog README HACKING
%{_bindir}/*
%{_mandir}/man1/*

