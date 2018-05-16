import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work.js';

const myWork = [
  {
    'title': "Manage AWS EC2 with Boto3",
    'href': "https://github.com/mikoSL/AWS_snapshot_analyzer",
    'desc': "Manage AWS EC2 instance snapshot with boto3.",
    'image': {
      'desc': "binary code picture",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "Serverless Video Sharing Website",
    'href': "http://serverless-videosharingapp-transcoded.s3-website-us-east-1.amazonaws.com",
    'desc': "Serverless and event-driven video sharing website with lambda,S3, Elastic Transcoder, Google Firebase and Autho0",
    'image': {
      'desc': "video sharing website",
      'src': "images/videosharingapp.png",
      'comment': ""
    }
  },
  {
    'title': "Work Example3",
    'href': "https://example.com",
    'desc': "add later 3.",
    'image': {
      'desc': "example screenshot of a project involving cats",
      'src': "images/example3.png",
      'comment': ""
    }
  }
];

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
