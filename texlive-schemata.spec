Name:		texlive-schemata
Version:	0.8
Release:	2
Summary:	Print topical diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/schemata
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates the creation of topical schemata,
outlines that use braces (or facsimiles thereof) to illustrate
the breakdown of concepts and categories in Scholastic thought
from late medieval and early modern periods.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/schemata
%doc %{_texmfdistdir}/doc/generic/schemata
#- source
%doc %{_texmfdistdir}/source/generic/schemata

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
