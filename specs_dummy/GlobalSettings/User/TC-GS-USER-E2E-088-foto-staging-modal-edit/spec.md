---
id: TC-GS-USER-E2E-088-foto-staging-modal-edit
title: 'Perubahan foto di modal Edit dibuang saat modal ditutup tanpa Save'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-543
coverage:
  web: automated
---

# Perubahan foto di modal Edit dibuang saat modal ditutup tanpa Save

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- User "Budi Santoso" punya foto profil A, dan berkas gambar B valid tersedia
- Pengamatan permintaan jaringan ke File Manager tersedia bagi skrip

## Test Steps

1. Klik row action `Edit` pada baris "Budi Santoso"
2. Ganti foto dengan berkas B (staged) atau klik `[Delete]` pada foto
3. Tutup modal dengan `✕`, atau dengan Esc pada percobaan kedua, tanpa `[Save]`
4. Verifikasi tidak ada permintaan ke File Manager yang sempat terkirim
5. Buka lagi User Detail "Budi Santoso" dan verifikasi Avatar tetap menampilkan foto A

## Notes

- Sumber `user.md` bagian 4.3 dan 4.4. Pasangan Edit dari `TC-GS-USER-E2E-087-foto-staging-modal-create`.
