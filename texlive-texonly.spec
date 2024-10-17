Name:		texlive-texonly
Version:	50985
Release:	2
Summary:	A sample document in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texonly
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texonly.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texonly.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A file written with TeX, not using any packgages or sty-files,
to be compiled with TeX or pdfTeX only, not with LaTeX et al.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/texonly

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
