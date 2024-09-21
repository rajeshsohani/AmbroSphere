window.onload = function() {
          let lastOpenedSubtopic = null;
        let lastOpenedDescription = null;

        // Function to show home content with mixed topics and subtopics
        function showHomeContent() {
            // Hide other content sections
            document.querySelectorAll('.content').forEach(content => content.style.display = 'none');
            // Show the home content section
            document.getElementById('homeContent').style.display = 'block';
            resetPage();
        }

        // Function to show content for the clicked subject
        function showContent(contentId) {
            var contents = document.querySelectorAll('.content');
            contents.forEach(function(content) {
                content.style.display = 'none';
            });

            // Hide home content when a specific topic is selected
            document.getElementById('homeContent').style.display = 'none';

            var content = document.getElementById(contentId);
            content.style.display = 'block';

            resetPage();
        }

        // Function to show or hide subtopics when a topic is clicked
        function toggleSubtopics(subtopicId) {
            var subtopics = document.getElementById(subtopicId);
            subtopics.style.display = (subtopics.style.display === "none" || subtopics.style.display === "") ? "block" : "none";
        }

        // Function to toggle description of subtopic
        function toggleDescription(subtopicId, description) {
            var descriptionDiv = document.getElementById('description');
            var subtopicElement = document.getElementById(subtopicId);

            if (lastOpenedDescription === description) {
                descriptionDiv.innerHTML = '';
                lastOpenedDescription = null;
            } else {
                descriptionDiv.innerHTML = description;
                lastOpenedDescription = description;
            }

            if (lastOpenedSubtopic && lastOpenedSubtopic !== subtopicElement) {
                lastOpenedSubtopic.style.display = 'none';
            }

            subtopicElement.style.display = (subtopicElement.style.display === "none" || subtopicElement.style.display === "") ? "block" : "none";
            lastOpenedSubtopic = subtopicElement;
        }

        // Function to reset the page when a new subject is selected
        function resetPage() {
            document.getElementById('description').innerHTML = '';
        }

        // Function to filter and search content
        function searchContent() {
            var searchTerm = document.getElementById('searchBar').value.toLowerCase();
            var topics = document.querySelectorAll('.topic, .subtopic');

            topics.forEach(function(topic) {
                var topicName = topic.dataset.topicName || topic.dataset.subtopicName;
                topic.style.display = topicName.toLowerCase().includes(searchTerm) ? 'block' : 'none';
            });
        }
};