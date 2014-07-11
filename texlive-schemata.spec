# revision 31743
# category Package
# catalog-ctan /macros/generic/schemata
# catalog-date 2013-09-24 17:34:21 +0200
# catalog-license lppl1.3
# catalog-version 0.7
Name:		texlive-schemata
Version:	0.7
Release:	7
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
%{_texmfdistdir}/tex/generic/schemata/schemata.sty
%doc %{_texmfdistdir}/doc/generic/schemata/Makefile
%doc %{_texmfdistdir}/doc/generic/schemata/README
%doc %{_texmfdistdir}/doc/generic/schemata/schemata.pdf
#- source
%doc %{_texmfdistdir}/source/generic/schemata/schemata.dtx
%doc %{_texmfdistdir}/source/generic/schemata/schemata.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
