---
id: TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1
title: "Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-69
  - TC-FA-LBL-70
  - TC-FA-LBL-71
  - TC-FA-LBL-73
  - TC-FA-LBL-80
  - TC-FA-LBL-81
coverage:
  web: automated
---

# Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Baseline jumlah total label katalog Company Alpha (N0) dicatat di hook `before` lewat fixture BE; tidak ada label yang dibuat spec ini (semua submit diblokir validasi).
- Nama 121 karakter untuk TC-FA-LBL-73 (hanya diketik, tidak disimpan): 19 kata `Alpha` + `Delta12` dipisah spasi tunggal.
- Emoji uji: `😊`; nilai `Promo 😊` untuk paste dan injeksi DOM.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog (jumlah total label).
- Kemampuan teknis: menempel teks dari clipboard dan menyetel nilai field langsung di DOM (bypass filter keystroke FE) untuk TC-FA-LBL-81.
- Spec ini tidak membuat data; tidak ada cleanup data.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-69: Label Name kosong membuat Submit disabled dengan tooltip

2. Hover `[Submit]`
3. Verifikasi `[Submit]` tampil dan berstatus disabled
4. Verifikasi tooltip `Enter a label name to continue.` tampil saat hover
5. Fokuskan `[Submit]` dengan keyboard
6. Verifikasi tooltip `Enter a label name to continue.` tampil saat fokus keyboard

### TC-FA-LBL-70: Label Name hanya berisi spasi dianggap kosong dan Submit disabled

7. Ketik tiga spasi di Label Name
8. Hover `[Submit]`
9. Verifikasi `[Submit]` berstatus disabled
10. Verifikasi tooltip `Enter a label name to continue.` tampil
11. Verifikasi jumlah total label katalog (lewat fixture BE) sama dengan N0, tidak ada label yang dibuat

### TC-FA-LBL-71: Enter pada Label Name kosong menampilkan pesan fallback V-01 tanpa membuat label

12. Hapus tiga spasi dari Label Name, klik Label Name, lalu tekan Enter tanpa mengisi
13. Verifikasi inline error `Label name must not be empty` tampil di bawah Label Name
14. Verifikasi modal tetap terbuka
15. Verifikasi tidak ada toast
16. Verifikasi jumlah total label katalog (lewat fixture BE) sama dengan N0, tidak ada label yang dibuat

### TC-FA-LBL-73: Label Name 121 karakter menampilkan V-02 dan Submit disabled

17. Ketik 121 karakter di Label Name
18. Hover `[Submit]`
19. Verifikasi inline error `Max. 120 characters` tampil
20. Verifikasi `[Submit]` berstatus disabled dengan tooltip `Max. 120 characters`

### TC-FA-LBL-80: Emoji diblok di level input saat diketik dan ditempel

21. Kosongkan Label Name lalu ketik karakter emoji `😊`
22. Verifikasi karakter emoji tidak masuk ke field (field tetap kosong)
23. Tempel teks `Promo 😊` dari clipboard
24. Verifikasi field hanya berisi `Promo `
25. Verifikasi tidak ada pesan error

### TC-FA-LBL-81: Emoji yang lolos filter input memunculkan fallback V-08

26. Kosongkan Label Name lalu injeksikan nilai `Promo 😊` langsung ke DOM field Label Name (bypass filter keystroke FE)
27. Hover `[Submit]`
28. Verifikasi inline error `Label name contains invalid characters` tampil langsung
29. Verifikasi `[Submit]` berstatus disabled dengan tooltip `Label name contains invalid characters`
30. Klik icon `[✕]`
31. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
32. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dipakai seluruh TC; Label Name dikosongkan atau diganti di antara kasus (prinsip 6). Nama yang diketik tidak pernah disimpan, jadi tidak memakai suffix.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 12, 21, dan 26 (mengosongkan isi Label Name dari TC di atasnya, digabung ke langkah TC berikutnya) dan langkah 32 (menutup modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Pembuktian "tidak ada label dibuat" pada TC-FA-LBL-70 butir c dan TC-FA-LBL-71 butir b memakai jumlah total label lewat fixture BE terhadap baseline N0 (S-12); TC tidak memberi langkah observasi lain.
- Temuan untuk QA:
  - TC-FA-LBL-69 Expected b menyebut tooltip tampil saat fokus keyboard pada `[Submit]` disabled; TC tidak menjelaskan cara memfokuskan elemen disabled. Spec mengikuti kalimat TC.
  - TC-FA-LBL-71 berlabel FE Test "Need API" tetapi Expected tidak memuat respons API; spec tidak memeriksa API selain jumlah label.
  - TC-FA-LBL-73 menyebut pesan muncul "real-time saat karakter ke-121 diketik"; spec mengetik 121 karakter dalam satu langkah dan tidak mengamati momen karakter ke-121 secara terpisah.
