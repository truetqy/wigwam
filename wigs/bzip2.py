class bzip2(Wig):
	tar_uri = 'http://www.bzip.org/1.0.6/bzip2-{RELEASE_VERSION}.tar.gz'
	last_release_version = '1.0.6'
	
	def setup(self):
		self.skip('configure')
		self.make_flags += [S.CFLAGS + '=' + S.FPIC_FLAG]
		self.make_install_flags += [S.PREFIX_MAKE_INSTALL_FLAG]
