class pip(Wig):
	git_uri = 'https://github.com/pypa/get-pip'
	raw_uri = 'https://bootstrap.pypa.io/get-pip.py'

	def setup(self):
		self.skip('configure', 'make')

	def gen_fetch_snippet(self):
		return [S.mkdir_p(self.paths.src_dir), P.download(self.raw_uri, os.path.join(self.paths.src_dir, os.path.basename(self.raw_uri)))]
	
	def gen_install_snippet(self):
		return ['python "%s" pip setuptools wheel' % os.path.join(self.paths.src_dir, os.path.basename(self.raw_uri))]
