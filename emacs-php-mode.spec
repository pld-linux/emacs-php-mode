%define		_orig_name	php-mode
%define		_emacs_version	21.2
%define		_php_mode_ver	1.0.2
#%define		_pack_ver	%(echo %{_php_mode_ver} | sed -e "s/\.//g")

Summary:	The Emacs php-mode text editor for the X Window System
Summary(de):	GNU Emacs php-mode
Summary(es):	GNU Emacs php-mode
Summary(fr):	GNU Emacs php-mode
Summary(pl):	GNU Emacs php-mode - Narzêdzia pomocnicze do PHP
Summary(pt_BR):	GNU Emacs php-mode
Summary(tr):	GNU Emacs php-mode
Name:		emacs-el-%{_orig_name}
Version:	%{_php_mode_ver}
Release:	1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/php-mode/%{_orig_name}-102.el
URL:		http://php-mode.sf.net/
Requires:	emacs-el = %{_emacs_version}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
php-mode - An Emacs major mode for editing PHP code. Features:
  - Syntax coloring and indenting;
  - Documentation browse and search functions;
  - Support for Imenu and SpeedBar;
  - Customization options.

%description -l pl
php-mode - rozszerzenie do Emacsa u³atwiaj±ce edycjê plików php.
Zalety:
  - kolorowanie sk³adni i indeksowanie;
  - Przegl±danie dokumentów i szukanie funkcji;
  - Wsparcie dla Imenu oraz SpeedBar;
  - Opcje dostosowania do w³asnych potrzeb.

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/%{_orig_name}.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/%{_orig_name}.el
