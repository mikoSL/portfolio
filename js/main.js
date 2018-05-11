import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
	{
		'title': "Example1",
		'image': {
			'desc': "example screenshot of a project involving code",
			'src': "images/example1.png",
			'comment':""
		}
	},
	{
		'title': "Example2",
		'image': {
			'desc': "example screenshot of a project involving chemistry",
			'src': "images/example2.png",
			'comment':""
		}
	},
	{
		'title': "Example3",
		'image': {
			'desc': "example screenshot of a project involving cat",
			'src': "images/example3.png",
			'comment':"pic srouce"
		}
	}
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));