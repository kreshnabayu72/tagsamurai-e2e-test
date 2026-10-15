---
id: TC-GS-GSET-E2E-007-guided-tooltip-konten-dan-navigasi-step
title: "Guided Tooltip: konten tiap step, navigasi Back/Done/replay, dan aksesibilitas keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-15
  - TC-GS-GSET-16
  - TC-GS-GSET-18
coverage:
  web: automated
---

# Guided Tooltip: konten tiap step, navigasi Back/Done/replay, dan aksesibilitas keyboard

## Prerequisites

- Login sebagai Role: Total Control dengan akun baru; flag `guided_tooltip_seen_gs-general-settings` belum ada
- User berada di Global Settings
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Konten Tiap Step

1. Buka Global Settings > General Settings
2. Amati Step 1
3. Verifikasi Step 1 menargetkan field Currency Code dengan title "Set Your Regional Format" dan description "Currency, time zone, and date/time format set here apply across every product — no need to configure them again per module."; tombol `[Back]` Hidden dan tombol `[Next]` tampil
4. Klik `[Next]`
5. Verifikasi Step 2 menargetkan field Session Idle Timeout dengan title "Control Session Timeout" dan description "Choose how long a user can stay idle before they're automatically logged out."; `[Back]` tampil dan tombol berubah menjadi `[Done]`

### Navigasi Back, Done, dan Replay

6. Klik `[Back]`
7. Verifikasi kembali ke Step 1
8. Klik `[Next]` lalu `[Done]`
9. Verifikasi walkthrough tertutup dan flag `seen` tersimpan
10. Klik tombol `[?]` di header halaman
11. Verifikasi walkthrough dimulai ulang dari Step 1 tanpa mereset flag `seen`

### Aksesibilitas Keyboard

12. Verifikasi tooltip box mendapat fokus keyboard
13. Tekan `→` (atau `Enter`)
14. Verifikasi pindah ke Step 2
15. Tekan `←`
16. Verifikasi kembali ke Step 1
17. Tekan `Esc`
18. Verifikasi walkthrough tertutup dan flag `seen` tersimpan (setara Skip)

## Notes

- Menggabungkan TC-GS-GSET-15, TC-GS-GSET-16, dan TC-GS-GSET-18 (konten dan navigasi Guided Tooltip). Spec 008 menangani trigger dan persistensi flag.
