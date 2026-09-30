---
id: TC-GS-USER-E2E-105-a11y-keyboard-dialog-dan-tooltip
title: 'Aksesibilitas keyboard: kontrol, tooltip, dan dialog'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-182
  - TC-GS-USER-183
  - TC-GS-USER-184
coverage:
  web: automated
---

# Aksesibilitas keyboard: kontrol, tooltip, dan dialog

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan baris yang punya toggle, checkbox, elemen Disabled bertooltip, dan dialog Delete

## Test Steps

1. Navigasi hanya dengan keyboard ke toggle Active, checkbox baris, date picker di Filter, dan chip input
2. Verifikasi semua kontrol itu bisa dioperasikan tanpa mouse
3. Fokuskan dengan keyboard elemen Disabled yang punya tooltip
4. Verifikasi tooltip muncul saat fokus, bukan hanya saat hover
5. Buka dialog konfirmasi Delete dan tekan `Tab` berulang
6. Verifikasi fokus tetap berada di dalam dialog dan tidak lompat ke elemen di belakang
7. Tekan `Esc`
8. Verifikasi dialog tertutup seperti klik `[Cancel]` dan user tidak terhapus

## Notes

- Sumber `user.md` bagian 4.4 dan `prd-conventions.md` bagian tentang aksesibilitas. TC sumber (`TC-GS-USER-182` sampai `184`) berstatus Manual; diotomasi sebagai pemeriksaan keyboard.
