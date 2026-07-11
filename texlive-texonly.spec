%global tl_name texonly
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2
Release:	%{tl_revision}.1
Summary:	A sample document in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/texonly
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texonly.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texonly.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A file written with TeX, not using any packages or sty-files, to be
compiled with TeX or pdfTeX only, not with LaTeX et al.

