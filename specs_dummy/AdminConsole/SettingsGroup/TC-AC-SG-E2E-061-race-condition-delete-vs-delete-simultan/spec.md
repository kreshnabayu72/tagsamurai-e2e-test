---
id: TC-AC-SG-E2E-061-race-condition-delete-vs-delete-simultan
title: "Konkurensi 2-Aktor: Same-action race Delete vs Delete simultan pada node yang sama"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-150
coverage:
  web: automated
---

# Konkurensi 2-Aktor: Same-action race Delete vs Delete simultan pada node yang sama

## Prerequisites

- Dua sesi browser independen (Aktor A dan Aktor B) login sebagai Total Control
- Node target X lolos guard Delete (Total Member = 0)

## Test Steps

### Eksekusi Balapan Delete vs Delete
1. Aktor A dan Aktor B sama-sama membuka dialog Delete pada node X yang sama
2. Aktor A menekan tombol konfirmasi `[Delete]` lebih dulu
3. Aktor B menekan tombol konfirmasi `[Delete]` tepat setelahnya (request B sampai server sesaat setelah A ter-commit)
4. Verifikasi Aktor A sukses menerima toast `"Success, group has been deleted."` dan record terhapus
5. Verifikasi Aktor B menerima respons 404/409 secara elegan (dialog tertutup, toast error terkelola, tabel auto-refresh)
6. Verifikasi sistem tidak mengalami crash 500 dan tidak terjadi double-delete atau duplicate Changelog

## Notes

- TC-AC-SG-112 s/d 116 (idempotensi backend & retry) dicakup pada pengujian backend.
