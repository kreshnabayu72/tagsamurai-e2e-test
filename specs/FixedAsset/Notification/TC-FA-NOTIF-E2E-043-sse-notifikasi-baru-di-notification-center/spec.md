---
id: TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center
title: "SSE: Notifikasi Baru di Notification Center menurut Sort, Tab, Search, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-172
  - TC-FA-NOTIF-173
  - TC-FA-NOTIF-174
  - TC-FA-NOTIF-175
  - TC-FA-NOTIF-176
coverage:
  web: automated
---

# SSE: Notifikasi Baru di Notification Center menurut Sort, Tab, Search, dan Filter

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar TC. Nilai (judul, transaksi `BRW-2026-0342`, kata Search, opsi Filter) dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pemicu: sesi API akun pemicu (akun tidak tertulis di Pre-setup TC; disediakan tim FE/BE) memicu notifikasi baru `borrow_waiting_approval` untuk akun aktor lewat fixture BE pemicu event. Pelaku kedua memakai sesi API, bukan sesi UI.
- Jendela absence SSE: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-172: Notifikasi baru muncul di Notification Center via SSE pada Sort Newest

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Catat jumlah item pada list (baseline)
3. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` untuk akun aktor hingga notifikasi tersimpan
4. Verifikasi item baru berjudul `Waiting for your approval` tampil di posisi teratas list tanpa memuat ulang halaman
5. Verifikasi jumlah item pada list bertambah 1 dari baseline langkah 2

### TC-FA-NOTIF-173: Notifikasi baru via SSE tidak disisipkan pada Sort Oldest

6. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
7. Klik toggle Sort hingga Sort `Oldest`
8. Catat nilai badge Bell icon serta judul dan isi item teratas list
9. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` untuk akun aktor hingga notifikasi tersimpan
10. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 8
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi item teratas list sama dengan item teratas yang dicatat pada langkah 8 (item baru tidak disisipkan di atas list)

### TC-FA-NOTIF-174: Notifikasi baru via SSE hanya disisipkan bila lolos Tab Unread

13. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
14. Klik Tab `Unread`
15. Catat jumlah item pada list (baseline)
16. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` (Unread) untuk akun aktor hingga notifikasi tersimpan
17. Verifikasi item baru berjudul `Waiting for your approval` tampil di posisi teratas Tab Unread
18. Verifikasi jumlah item pada list bertambah 1 dari baseline langkah 15

### TC-FA-NOTIF-175: Notifikasi baru via SSE tidak disisipkan bila tidak lolos Search aktif

19. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
20. Ketik Search `repaired`, tekan Enter
21. Verifikasi list tersaring dan memuat item `Asset has been repaired`
22. Catat nilai badge Bell icon
23. Lewat sesi API akun pemicu, picu notifikasi `borrow_waiting_approval` baru untuk akun aktor hingga notifikasi tersimpan
24. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 22
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Verifikasi item `Waiting for your approval` tidak tampil pada list karena tidak mengandung `repaired`

### TC-FA-NOTIF-176: Notifikasi baru via SSE tidak disisipkan bila tidak lolos Filter Event Type aktif

27. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
28. Klik icon Filter, pilih Event Type `Damaged Repaired`, lalu klik `[Apply]`
29. Verifikasi list memuat item `Asset has been repaired`
30. Catat nilai badge Bell icon
31. Lewat sesi API akun pemicu, picu notifikasi `borrow_waiting_approval` baru untuk akun aktor hingga notifikasi tersimpan
32. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 30
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Verifikasi item `borrow_waiting_approval` (`Waiting for your approval`) tidak tampil pada list
35. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (precondition TC "User berada di Notification Center"), 6, 13, 19, 27 (pemulihan seed, muat ulang, dan masuk kembali lewat `[Show All]` yang mereset Tab, Search, Sort, dan Filter ke default; perilaku reset ini juga diasersi spec 114), 35 (pemulihan Filter).
- Asersi tambahan di luar Expected TC (S-03): langkah 5, 18 (jumlah item +1, pembeda terhadap N-01 yang berjudul sama), langkah 10, 24, 32 (badge +1 sebagai anchor positif bahwa notifikasi terkirim sebelum asersi absence; bagian 6 dan 8b butir 11), langkah 21 dan 29 (item pembanding sebelum asersi absence).
- Urutan asersi pada TC-173, 175, 176 (badge, tunggu 5 detik, baru absence) menyimpang dari urutan Expected TC karena anchor positif harus mendahului absence (8b butir 2 dan 5).
- Spec ini sekitar 35 langkah: kelima TC berbagi topik, seed, dan pemicu yang sama, dan tiap blok berdiri sendiri karena seed dipulihkan di antara blok.
- Temuan untuk QA:
  - TC-172 sampai 176 menulis "akun lain" tanpa menyebut akun pemicu; TC-172, 173, 174 tidak menyebut jenis event yang dipicu. Spec memakai `borrow_waiting_approval` mengikuti TC-175, 176, 180.
  - TC-174 menulis "view-only/actionable Unread" pada Expected; spec memakai event actionable.
