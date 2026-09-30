---
id: TC-GS-USER-E2E-087-foto-staging-modal-create
title: 'Foto di modal Create hanya staged sampai Submit dan dibuang saat modal ditutup'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-537
  - TC-GS-USER-538
  - TC-GS-USER-539
coverage:
  web: automated
---

# Foto di modal Create hanya staged sampai Submit dan dibuang saat modal ditutup

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Berkas gambar valid (PNG atau JPG) tersedia untuk dipilih lewat file picker
- Pengamatan permintaan jaringan ke File Manager tersedia bagi skrip

## Test Steps

1. Klik `[+ User]` lalu hover field Photo sebelum memilih berkas
2. Verifikasi overlay `[Edit]` saja tampil, tanpa `[Delete]`
3. Pilih berkas gambar lewat `[Edit]`
4. Hover field Photo lagi dan verifikasi overlay berubah menjadi `[Edit]` dan `[Delete]`
5. Klik `[Delete]`
6. Verifikasi field Photo kembali kosong (avatar inisial) dan tidak ada permintaan ke File Manager
7. Pilih berkas gambar lagi lalu tutup modal dengan `✕`, atau dengan Esc pada percobaan kedua
8. Verifikasi modal tertutup, tidak ada berkas baru yang tercipta di File Manager, dan tidak ada user yang dibuat

## Notes

- Sumber `user.md` bagian 4.3, 4.4, dan `prd-conventions.md` (File Upload Photo: picker difilter PNG/JPG, foto lebih dari 1 MB diubah ukurannya otomatis). Foto di Create dan Edit modal bersifat staged dan baru tersimpan saat Submit.
- Bila muncul dialog konfirmasi buang perubahan saat menutup modal, konfirmasi dialog itu.
