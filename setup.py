from distutils.core import setup
setup(
  name = 'calc',         
  packages = ['calc'],   
  version = '1.0',      
  license='MIT',        
  description = 'This package returns addition or multiplication of two integers.',   
  url = 'https://github.com/YugantM/python_calc_module',   
  download_url = 'https://github.com/YugantM/python_calc_module.git',  
  install_requires=[
          'add',
          'mul'
      ],  
  entry_points = {
              'console_scripts': ['calc = calc.__main__:main',],
              },
  scripts=['scripts/calc'],  
  
  keywords = ['add','multiplication', 'calculation'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
