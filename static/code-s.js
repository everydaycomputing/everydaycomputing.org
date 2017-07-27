var elements = [];
var type = 0;
$(function() {
  console.log(elements)
  // on dom ready
  // console.log("hi");
  var cy = cytoscape({
    container: document.getElementById("cy"),

    boxSelectionEnabled: false,
    autounselectify: true,

    elements: elements, //{
    //   nodes: [
    //     {
    //       data: {
    //         id: "1U",
    //         clicked_var: 0,
    //         algs: "1, 2, 3",
    //         ulgs: "3, 2",
    //         temp_name:
    //           "Understand that a condition is a statement that can be classified as true or false. \n \n Assess truth-value of a condition.",
    //         name:
    //           "Understand that a condition is a statement that can be classified as true or false. \n \n Assess truth-value of a condition.",
    //         href: [
    //           {
    //             url: "http://maroonstack.com",
    //             text:
    //               'Liu, Jiangjiang Lin, Cheng-Hsien Wilson, Joshua Hemmenway, David Hasson, Ethan Barnett, Zebulun Xu, Yingbo . "Making games a snap with Stencyl: a summer computing workshop for K-12 teachers." (2014). 169-174.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3Jnci4LEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiDWxpdTIwMTRtYWtpbmcM/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "beginning unplugged"
    //     },
    //     //
    //     {
    //       data: {
    //         id: "2U",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that a conditional is a statement that connects a condition to a corresponding consequence or outcome. \n \n Make decisions based on conditionals.",
    //         name:
    //           "Understand that a conditional is a statement that connects a condition to a corresponding consequence or outcome. \n \n Make decisions based on conditionals.",
    //         href: [
    //           {
    //             text:
    //               'Franklin, Diana Conrad, Phillip Aldana, Gerardo Hough, Sarah . "Animal tlatoque: attracting middle school students to computing through culturally-relevant themes." None. (2011). 453-458.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmZyYW5rbGluMjAxMWFuaW1hbAw/"
    //           },
    //           {
    //             text:
    //               'Werner, Linda Denner, Jill Campe, Shannon Kawamoto, Damon Chizuru . "The fairy performance assessment: measuring computational thinking in middle school." None. (2012). 215-220.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiD3dlcm5lcjIwMTJmYWlyeQw/"
    //           },
    //           {
    //             text:
    //               'Guzdial, Mark . "Education Paving the way for computational thinking." Communications of the ACM. (2008). 25-27.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjULEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiFGd1emRpYWwyMDA4ZWR1Y2F0aW9uDA/"
    //           },
    //           {
    //             text:
    //               'Grover, Shuchi Cooper, Stephen Pea, Roy . "Assessing Computational Learning in K-12." None. (2014). 57-62.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JnckALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiH0dyb3ZlcjoyMDE0OkFDTDoyNTkxNzA4LjI1OTE3MTMM/"
    //           },
    //           {
    //             text:
    //               'Basu, Satabdi Kinnebrew, John S Biswas, Gautam . "Assessing student performance in a computational-thinking based science learning environment." None. (2014). 476-481.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjILEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEWJhc3UyMDE0YXNzZXNzaW5nDA/"
    //           },
    //           {
    //             text:
    //               'Flatland, Robin Lim, Darren Matthews, James Vandenberg, Scott . "Supporting CS10K: A new computer science methods course for mathematics education students." None. (2015). 302-307.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjcLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiFmZsYXRsYW5kMjAxNXN1cHBvcnRpbmcM/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "beginning unplugged"
    //     },

    //     //
    //     {
    //       data: {
    //         id: "1.1U",
    //         // clicked_var: 0,
    //         temp_name:
    //           "Understand that a Boolean is a variable with values T or F. \n \n Use a Boolean variable.",
    //         name:
    //           "Understand that a Boolean is a variable with values T or F. \n \n Use a Boolean variable.",
    //         href: [
    //           {
    //             text:
    //               'Liu, Jiangjiang Lin, Cheng-Hsien Hasson, Ethan Philip Barnett, Zebulun David . "Introducing computer science to K-12 through a summer computing workshop for teachers." (2011). 389-394.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmxpdTIwMTFpbnRyb2R1Y2luZww/"
    //           },
    //           {
    //             text:
    //               'Grover, Shuchi Pea, Roy Cooper, Stephen . "Designing for deeper learning in a blended computer science course for middle school students." Computer Science Education. (2015). 199-237.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjQLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiE2dyb3ZlcjIwMTVkZXNpZ25pbmcM/"
    //           }
    //         ]
    //       },
    //       position: { x: 150, y: 0 },
    //       grabbable: false,
    //       classes: "advanced programming"
    //     },
    //     //
    //     {
    //       data: {
    //         id: "6bU",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that conditional operators such as AND and OR can be used to express compound conditions. \n \nUse conditional operators to create compound conditions in conditional statements.",
    //         name:
    //           "Understand that conditional operators such as AND and OR can be used to express compound conditions. \n \nUse conditional operators to create compound conditions in conditional statements.",
    //         href: [
    //           {
    //             text:
    //               'Liu, Jiangjiang Lin, Cheng-Hsien Hasson, Ethan Philip Barnett, Zebulun David . "Introducing computer science to K-12 through a summer computing workshop for teachers." None. (2011). 389-394.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmxpdTIwMTFpbnRyb2R1Y2luZww/"
    //           },
    //           {
    //             text:
    //               'Grover, Shuchi Pea, Roy Cooper, Stephen . "Designing for deeper learning in a blended computer science course for middle school students." Computer Science Education. (2015). 199-237.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjQLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiE2dyb3ZlcjIwMTVkZXNpZ25pbmcM/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "advanced programming"
    //     },
    //     //
    //     {
    //       data: {
    //         id: "1.2U",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that often there are multiple conditions to be considered in a situation. \n \n List all the conditions that you might need to consider when solving a problem.",
    //         name:
    //           "Understand that often there are multiple conditions to be considered in a situation. \n \n List all the conditions that you might need to consider when solving a problem.",
    //         href: [
    //           {
    //             text:
    //               'Franklin, Diana Conrad, Phillip Aldana, Gerardo Hough, Sarah . "Animal tlatoque: attracting middle school students to computing through culturally-relevant themes." None. (2011). 453-458.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmZyYW5rbGluMjAxMWFuaW1hbAw/"
    //           },
    //           {
    //             text:
    //               'Armoni, Michal Gal-Ezer, Judith . "Early computing education: why? what? when? who?." ACM Inroads. (2014). 54-59.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiD2FybW9uaTIwMTRlYXJseQw/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "intermediate unplugged"
    //     },
    //     {
    //       data: {
    //         id: "4.1U",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that sometimes conditions overlap, and more than one can be applicable at a time. \n \n Identify examples of overlapping conditions. Create and interpret conditionals that consider how conditions overlap.",
    //         name:
    //           "Understand that sometimes conditions overlap, and more than one can be applicable at a time. \n \n Identify examples of overlapping conditions. Create and interpret conditionals that consider how conditions overlap.",
    //         href: [
    //           {
    //             text:
    //               'Franklin, Diana Conrad, Phillip Aldana, Gerardo Hough, Sarah . "Animal tlatoque: attracting middle school students to computing through culturally-relevant themes." None. (2011). 453-458.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmZyYW5rbGluMjAxMWFuaW1hbAw/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "intermediate unplugged"
    //     },
    //     {
    //       data: {
    //         id: "3aU",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that it may be necessary to specify an outcome to correspond with BOTH states of a condition (true and false). \n \n Consider both states of a condition when creating conditional statements.",
    //         name:
    //           "Understand that it may be necessary to specify an outcome to correspond with BOTH states of a condition (true and false). \n \n Consider both states of a condition when creating conditional statements.",
    //         href: [
    //           {
    //             text:
    //               'Armoni, Michal Gal-Ezer, Judith . "Early computing education: why? what? when? who?." ACM Inroads. (2014). 54-59.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiD2FybW9uaTIwMTRlYXJseQw/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "beginning unplugged"
    //     },
    //     //
    //     {
    //       data: {
    //         id: "4U",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that computers require all actions to be specified, and that you have to create a conditional to prompt a computer to complete each action. \n \n Make a complete list of the required actions and their associated conditions, and create the necessary conditionals.",
    //         name:
    //           "Understand that computers require all actions to be specified, and that you have to create a conditional to prompt a computer to complete each action. \n \n Make a complete list of the required actions and their associated conditions, and create the necessary conditionals.",
    //         href: [
    //           {
    //             text:
    //               'Guzdial, Mark . "Education Paving the way for computational thinking." Communications of the ACM. (2008). 25-27.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjULEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiFGd1emRpYWwyMDA4ZWR1Y2F0aW9uDA/”"
    //           },
    //           {
    //             text:
    //               'Franklin, Diana Conrad, Phillip Aldana, Gerardo Hough, Sarah . "Animal tlatoque: attracting middle school students to computing through culturally-relevant themes." None. (2011). 453-458.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmZyYW5rbGluMjAxMWFuaW1hbAw/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "intermediate programming"
    //     },

    //     {
    //       data: {
    //         id: "5U",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that command such as if-then, if-then-else, and event handlers signal a computer to evaluate conditions and decide how to act based on conditions. \n \n Create a program with conditionals.",
    //         name:
    //           "Understand that command such as if-then, if-then-else, and event handlers signal a computer to evaluate conditions and decide how to act based on conditions. \n \n Create a program with conditionals.",
    //         href: [
    //           {
    //             text:
    //               'Liu, Jiangjiang Lin, Cheng-Hsien Hasson, Ethan Philip Barnett, Zebulun David . "Introducing computer science to K-12 through a summer computing workshop for teachers." None. (2011). 389-394.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmxpdTIwMTFpbnRyb2R1Y2luZww/"
    //           },
    //           {
    //             text:
    //               'Werner, Linda Denner, Jill Campe, Shannon Kawamoto, Damon Chizuru . "The fairy performance assessment: measuring computational thinking in middle school." None. (2012). 215-220.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiD3dlcm5lcjIwMTJmYWlyeQw/"
    //           },
    //           {
    //             text:
    //               'Franklin, Diana Conrad, Phillip Aldana, Gerardo Hough, Sarah . "Animal tlatoque: attracting middle school students to computing through culturally-relevant themes." None. (2011). 453-458.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEmZyYW5rbGluMjAxMWFuaW1hbAw/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "beginning programming"
    //     },

    //     {
    //       data: {
    //         id: "3bU",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand conditional branching, that is, the reach of the effects of a conditional statement and how conditionals can affect the path of execution. \n \n Use the if/else construct to divert the default pathway through a program. Create different pathways in programs using conditional statements.",
    //         name:
    //           "Understand conditional branching, that is, the reach of the effects of a conditional statement and how conditionals can affect the path of execution. \n \n Use the if/else construct to divert the default pathway through a program. Create different pathways in programs using conditional statements.",
    //         href: [
    //           {
    //             text:
    //               'Werner, Linda Denner, Jill Campe, Shannon . "Children programming games: a strategy for measuring computational learning." ACM Transactions on Computing Education TOCE. (2015). 24',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjMLEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEndlcm5lcjIwMTVjaGlsZHJlbgw/"
    //           },
    //           {
    //             text:
    //               'Werner, Linda Denner, Jill Campe, Shannon Kawamoto, Damon Chizuru . "The fairy performance assessment: measuring computational thinking in middle school." None. (2012). 215-220.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjALEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiD3dlcm5lcjIwMTJmYWlyeQw/"
    //           },
    //           {
    //             text:
    //               'Peluso, Eileen M Sprechini, Gene . "The Impact of Alice on the Attitudes of High School Students Toward Computing."',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3Jnci0LEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiDHBlbHVzb2ltcGFjdAw/"
    //           },
    //           {
    //             text:
    //               'Liu, Jiangjiang Lin, Cheng-Hsien Wilson, Joshua Hemmenway, David Hasson, Ethan Barnett, Zebulun Xu, Yingbo . "Making games a snap with Stencyl: a summer computing workshop for K-12 teachers." None. (2014). 169-174.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3Jnci4LEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiDWxpdTIwMTRtYWtpbmcM/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "intermediate programming"
    //     },

    //     {
    //       data: {
    //         id: "6aU",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand that conditional statements can be nested or combined in different ways to accomplish complex goals. \n \n Combine conditions using nesting or other techniques to accomplish complex goals.",
    //         name:
    //           "Understand that conditional statements can be nested or combined in different ways to accomplish complex goals. \n \n Combine conditions using nesting or other techniques to accomplish complex goals.",
    //         href: []
    //       },
    //       grabbable: false,
    //       classes: "intermediate unplugged"
    //     },

    //     {
    //       data: {
    //         id: "7aU",
    //         clicked_var: 0,
    //         temp_name:
    //           "Understand how to evaluate and apply different approaches to combining conditional statements for particular problem.",
    //         name:
    //           "Understand how to evaluate and apply different approaches to combining conditional statements for particular problem.",
    //         href: [
    //           {
    //             text:
    //               'Harms, Kyle J Rowlett, Noah Kelleher, Caitlin . "Enabling independent learning of programming concepts through programming completion puzzles." None. (2015). 271-279.',
    //             link:
    //               "http://everydaycomputing.org/resource/article/ahZzfmV2ZXJ5ZGF5Y29tcHV0aW5nb3JncjILEgdBcnRpY2xlIgdhcnRpY2xlDAsSB0FydGljbGUiEWhhcm1zMjAxNWVuYWJsaW5nDA/"
    //           }
    //         ]
    //       },
    //       grabbable: false,
    //       classes: "advanced programming"
    //     }

    //     //
    //   ], // close nodes

    //   edges: [
    //     {
    //       data: {
    //         source: "1U",
    //         target: "1.1U",
    //         label: "A"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "1U",
    //         target: "1.2U",
    //         label: "B"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "1U",
    //         target: "2U",
    //         label: "C"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "1.1U",
    //         target: "6bU",
    //         label: "D"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "1.2U",
    //         target: "4.1U",
    //         label: "E"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "2U",
    //         target: "3aU",
    //         label: "F"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "3aU",
    //         target: "5U",
    //         label: "G"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "2U",
    //         target: "5U",
    //         label: "H"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "4.1U",
    //         target: "4U",
    //         label: "I"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "6bU",
    //         target: "4U",
    //         label: "J"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "5U",
    //         target: "3bU",
    //         label: "K"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "4U",
    //         target: "6aU",
    //         label: "L"
    //       }
    //     },
    //     {
    //       data: {
    //         source: "6aU",
    //         target: "7aU",
    //         label: "M"
    //       }
    //     }
    //   ]
    //},

    layout: {
      name: "breadthfirst",
      directed: true,

      padding: 100,
      //name: 'preset',
      fit: true,
      avoidOverlap: true,
      avoidOverlapPadding: 150,
      spacingFactor: 1.8
    },

    ready: function() {
      window.cy = this;
    },

    style: [
      {
        selector: "edge",
        style: {
          width: "4",
          "target-arrow-shape": "triangle",
          "curve-style": "bezier",
          "control-point-step-size": 40,
          label: "data(label)",
          "font-family": "liberation-sans, sans-serif",
          "font-weight": "600",
          "font-size": "60"
        }
      },
      {
        selector: "node",
        style: {
          shape: "roundrectangle",
          "text-wrap": "wrap",
          "text-max-width": 225,
          "text-valign": "center",
          "font-family": "liberation-sans, sans-serif",
          "font-weight": "600",
          "font-size": "17",
          "border-width": "4px 0px 4px 0px",
          height: 250,
          width: 250,
          padding: 10,
          label: "data(name)"
        }
      },
      {
        selector: "node.beginning",
        style: {
          // "border-width": 4,
          "border-color": "green",
          "border-style": "solid"
        }
      },
      {
        selector: "node.intermediate",
        style: {
          // "border-width": 4,
          "border-color": "orange",
          "border-style": "solid"
        }
      },
      {
        selector: "node.advanced",
        style: {
          // "border-width": 4,
          "border-color": "purple",
          "border-style": "solid"
        }
      },
      {
        selector: "node.unplugged",
        style: {
          "background-color": "#c6c6c6",
          color: "#0169D9"
        }
      },
      {
        selector: "node.programming",
        style: {
          "background-color": "white"
        }
      }
    ]
  });

  // you can use qtip's regular options
  // see http://qtip2.com/

  // cy.$('*').qtip({
  // content: 'Hello!',
  // position: {
  // my: 'top center',
  // at: 'bottom center'
  // },
  // style: {
  // classes: 'qtip-bootstrap',
  // tip: {
  // width: 16,
  // height: 8
  // }
  // }
  // });

  // cy.nodes().qtip({
  //   content: function(){
  //     var links = ""
  //     json = eval(this.data('href'));
  //     console.log(json);
  //     json.forEach(function(entry) {
  //       linkData = eval(entry)
  //       console.log(entry);
  //       links = links + '<li><a target="_blank" href="'+linkData['link']+'">'+linkData['text']+'</a></li>';
  //     });
  //     //return this.data('href');
  //     return links;
  //   }
  // });
  // cy.userPanningEnabled(false);
  // cy.boxSelectionEnabled(false);
  // cy.zoom(0.3);
  // cy.zoomingEnabled(false);
  function rotate() {
    setTimeout(function() {
      cy.nodes().positions(function(node, i) {
        return {
          x: node.position("y") * 0.8,
          y: -1 * node.position("x") * 0.7
        };
      });
      cy.fit();
    }, 100);
  }
  rotate();

  // cy.contextMenus({
  //   menuItems: [
  //     {
  //       id: "action_lgs",
  //       content: "Action Learning Goals",
  //       selector: "node",
  //       onClickFunction: function(event) {
  //         var target = event.target || event.cyTarget;
  //         target.data("name", target.data("algs"));
  //         cy
  //           .style()
  //           .selector(target)
  //           .style({
  //             "font-size": "60"
  //             // 'background-color': 'yellow'
  //           })
  //           .update();
  //         var win = window.open(target.data("href")[0]["link"]);
  //         if (!win) {
  //           alert("Please allow popups");
  //         }
  //         // target.style({'font-size': "17"});
  //       }
  //     },
  //     {
  //       id: "understanding_lgs",
  //       content: "Understanding Learning Goals",
  //       selector: "node",
  //       onClickFunction: function(event) {
  //         var target = event.target || event.cyTarget;
  //         target.data("name", target.data("ulgs"));
  //         // target.style({'font-size': "17"});
  //         // console.log(target.position("y"));
  //         cy
  //           .style()
  //           .selector(target)
  //           .style({
  //             "font-size": "60"
  //             // 'background-color': 'yellow'
  //           })
  //           .update();
  //         var win = window.open(target.data("href")["url"]);
  //         if (!win) {
  //           alert("Please allow popups");
  //         }
  //       }
  //     },
  //     {
  //       id: "arrow_activities",
  //       content: "Arrow Activities",
  //       selector: "edge",
  //       onClickFunction: function(event) {
  //         var target = event.target || event.cyTarget;
  //         target.data("label", target.data("source"));
  //       }
  //     }
  //   ]
  // });

  var advancedButton = document.getElementById("advanced");
  advancedButton.addEventListener("click", function() {
    cy.$("*").show();
  });

  var intermediateButton = document.getElementById("intermediate");
  intermediateButton.addEventListener("click", function() {
    cy.$("*").show();
    cy.$(".advanced").hide();
  });

  var beginningtButton = document.getElementById("beginning");
  beginningtButton.addEventListener("click", function() {
    cy.$("*").show();
    cy.$(".advanced").hide();
    cy.$(".intermediate").hide();
  });
  //
  //
  /*
cy.on('tap', 'node', function(){
try { // your browser may block popups
window.open( this.data('href') );
} catch(e){ // fall back on url change
window.location.href = this.data('href');
}
});
*/
  // function fn1() {
  //   return 'hi';
  // }
  cy.nodes().on("mouseover", function() {
    cy
      .style()
      .selector(this)
      .style({
        "border-color": "black",
        "border-width": "7px"
        // 'background-color': 'yellow'
      })
      .update(); // update the elements in the graph with the new style
  });
  cy.nodes().on("mouseout", function() {
    cy
      .style()
      .selector(this)
      .style({
        "border-color": function(node) {
          if (node.hasClass("beginning")) {
            return "green";
          } else if (node.hasClass("intermediate")) {
            return "orange";
          } else {
            return "purple";
          }
        },
        "border-width": "4px"
        // 'background-color': 'yellow'
      })
      .update(); // update the elements in the graph with the new style
  });


  cy.nodes().on("click", function() {
    //   cy.style()
    //     .selector(this)
    //     .style({
    //       'border-color' : 'black'
    //     // 'background-color': 'yellow'
    //   })

    // .update() // update the elements in the graph with the new style
    function fn1(node) {
      function fn_x(node) {
        return node.renderedPosition("x");
      }
      function fn_y(node) {
        return node.renderedPosition("y");
      }
      if (node.data("clicked_var") == 1) {
        node.data("clicked_var", 0);
        // document.getElementById("my-btn").style.visibility = "hidden";
        cy
          .style()
          .selector(node)
          .style({
            "font-size": "17"
            // 'background-color': 'yellow'
          })
          .update();
        return node.data("temp_name");
      } else {
        var collection = cy.nodes();
        function get_name(ele) {
          return ele.data("temp_name");
        }
        collection.map(function change_name(ele) {
          ele.data("name", get_name(ele));
          cy
            .style()
            .selector(ele)
            .style({
              "font-size": "17"
            })
            .update();
        });
        node.data("clicked_var", 1);
        // document.getElementById("my-btn").style.visibility = "visible";
        // document.getElementById("my-btn").style.border = "solid";
        // document.getElementById("my-btn").style.borderColor = "black";
        // document.getElementById("my-btn").style.border = "solid";
        // document.getElementById("my-btn").style.borderWidth = "2px";
        // console.log("x :" + fn_x(node));
        // document.getElementById("my-btn").style.left = 47 + fn_x(node) + "px"; //548 + fn_x(node) * 0.546 + "px";//fn2(node) + "px";
        // console.log("y :" + fn_y(node));
        // document.getElementById("my-btn").style.top = 50 + fn_y(node) + "px"; //40 + fn_y(node) * -0.546 + "px";
        cy
          .style()
          .selector(node)
          .style({
            "font-size": "80"
            // 'background-color': 'yellow'
          })
          .update(); // update the elements in the graph with the new style
        return node.data("id");
      }
    }
    this.data({ name: fn1(this) });

    // window.open('http://maroonstack.com')

    //   cy.$('node:selected').neighborhood('edge').style({
    //   'line-color': 'black'
    // }); console.log('hi');
  });

}); // on dom ready

// function clear_elements() {
//   elements = { nodes: [], edges: [] };
// }

// function accept_data(input) {
//   // input = JSON.parse(input);
//   // console.log(input);
//   alert(input);
//   if (type == 0) {
//     type = 1;
//     for (node in input[0]) {
//       var data = node.data; //["data"];
//       var id = data.id; //data["id"];
//       var name = data.name; //data["name"];
//       var temp_name = name;
//       var clicked_var = 0;
//       var href = [];
//       var classes = node.classes; //node["classes"];
//       var grabbable = false;
//       data = {
//         id: id,
//         clicked_var: clicked_var,
//         temp_name: temp_name,
//         name: name,
//         href: href
//       };
//       elements[nodes].append({
//         data: data,
//         grabbable: grabbable,
//         classes: classes
//       });
//     }
//   } else {
//     type = 0;
//     for (arrow in input[1]) {
//       var data = arrow.data; //["data"];
//       var label = data.data; //["label"];
//       var source = data.source; //["source"];
//       var target = data.target; //["target"];
//       var unplugged = data.unplugged; //["unplugged"];
//       data = {
//         source: source,
//         target: target,
//         label: label,
//         unplugged: unplugged
//       };
//       elements[edges].append({ data: data });
//     }
//   }
// }

function accept_data(input) {
  if(!('classes' in input)) {
    var data = input.data;
    console.log(data)
    var source = data.source;
    var target = data.target;
    var label = data.label;
    var unplugged = data.unplugged;
    console.log(label);
    elements.push({data : {source : source, target : target, label : label, unplugged : unplugged}});
  } else {
    var data = input.data;
    console.log(data);
    var classes = input.classes;
    var id = data.id;
    var name = data.name;
    var temp_name = data.temp_name;
    var clicked_var = data.clicked_var;
    var href = data.href;
    // var classes = class_dict.classes;
    console.log(id);
    elements.push({data : {id : id, temp_name : temp_name, name : name, clicked_var : clicked_var, href : href}, 
      grabbable : false, classes : classes});
  }

}
