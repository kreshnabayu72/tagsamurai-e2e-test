---
id: TC-FA-NOTIF-E2E-009-aksesibilitas-keyboard-dropdown-panel-dan-notification-center
title: "Aksesibilitas Keyboard Dropdown Panel dan Notification Center"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-32
  - TC-FA-NOTIF-33
coverage:
  web: automated
---

# Aksesibilitas Keyboard Dropdown Panel dan Notification Center

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor. TC-33 menandai N-03 menjadi Read; fixture BE pemulih seed dijalankan di hook `before` dan `after` dan memulihkannya. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Mark as Read pada seed notifikasi N-03 (Pre-setup #17) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis: pengiriman keystroke ke browser (`Tab`, `Enter`, `Esc`) dan pembacaan elemen yang sedang fokus.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-32: Accessibility Dropdown Panel: navigasi keyboard dan focus trap

1. Fokuskan Bell icon dengan tombol Tab, lalu tekan Enter
2. Verifikasi Dropdown Panel terbuka
3. Tekan Tab berulang kali sampai melewati item terakhir
4. Verifikasi fokus berputar di dalam Dropdown Panel dan tidak keluar ke elemen di belakang panel selama panel terbuka
5. Tekan Esc
6. Verifikasi Dropdown Panel tertutup
7. Verifikasi fokus kembali ke Bell icon

### TC-FA-NOTIF-33: Accessibility Notification Center: navigasi keyboard

8. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
9. Tekan Tab berurutan dari Breadcrumb sampai item pertama
10. Verifikasi fokus bergerak berurutan melewati Tab, Search, Filter, Sort, lalu item list
11. Tekan Tab sampai fokus berada pada tombol `[Mark as Read]` item N-03, lalu tekan Enter
12. Verifikasi tombol `[Mark as Read]` item N-03 dapat dioperasikan dengan Enter (tombol tidak lagi tampil pada item N-03)
13. Verifikasi item N-03 menjadi Read dengan Title tidak bold
14. Verifikasi dot tidak tampil pada item N-03

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 8 (buka Notification Center; TC-33 menulis "Buka Notification Center"), langkah 11 (bagian "Tekan Tab sampai fokus berada pada tombol `[Mark as Read]` item N-03" memenuhi Langkah TC-33 "Pada tombol `[Mark as Read]` item N-03 tekan Enter").
- Urutan langkah 6 dan 7 mengikuti state: fokus diasersi segera setelah panel tertutup (8b butir 5).
- Pemulihan N-03 ke Unread dilakukan fixture BE pemulih di hook `after` (state berakhir tanpa form dirty).
- Spec 009 mengubah N-03 menjadi Read pada seed yang juga dibaca spec 002; keduanya dibedakan per topik (aksesibilitas keyboard vs screening Dropdown Panel) dengan seed dipulihkan fixture BE di hook.
- Temuan untuk QA:
  - TC-33 Expected a menulis "melewati Tab, Search, Filter, Sort"; ketiga kontrol itu dan Tab diasumsikan fokus berurutan tanpa menyebut apakah Tab `All` dan `Unread` dihitung satu atau dua stop fokus. Spec mengasersi urutan sesuai teks TC.
