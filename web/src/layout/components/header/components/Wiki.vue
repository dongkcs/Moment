<template>
  <n-icon
    mr-20
    size="18"
    style="cursor: pointer"
    :title="$t('header.label_wiki')"
    @click="handleLinkClick"
  >
    <TheIcon icon="mdi:file-document-outline" :size="18" />
  </n-icon>
</template>

<script setup>
function handleLinkClick() {
  window.open('https://github.com/Robert-Stackflow/Moment/wiki')
}
</script>
