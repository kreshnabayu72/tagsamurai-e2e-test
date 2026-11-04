---
id: TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik
title: "Filter Panel: Draft Dibuang, Clear Field, dan Indikator Titik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-209
  - TC-FA-NOTIF-210
  - TC-FA-NOTIF-214
  - TC-FA-NOTIF-427
coverage:
  web: automated
---

# Filter Panel: Draft Dibuang, Clear Field, dan Indikator Titik

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-209: Menutup Filter Panel tanpa Apply membuang draft

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Catat judul item teratas list dan jumlah item yang termuat (baseline)
3. Klik icon Filter, centang `Damaged Repaired`
4. Klik di luar panel
5. Klik icon Filter lagi
6. Verifikasi panel menampilkan nilai ter-Apply terakhir (kosong)
7. Verifikasi judul item teratas dan jumlah item yang termuat sama dengan baseline langkah 2 (list tidak berubah)
8. Verifikasi badge titik tidak muncul pada icon Filter

### TC-FA-NOTIF-210: [Clear Field] mengosongkan Filter dan [Apply] menghapus indikator titik

9. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
10. Klik icon Filter, centang `Damaged Repaired`, lalu klik `[Apply]`
11. Klik `[Clear Field]`, lalu klik `[Apply]`
12. Verifikasi list kembali memuat semua data pada Tab aktif (item `Waiting for your approval` tampil)
13. Verifikasi badge titik pada icon Filter hilang

### TC-FA-NOTIF-214: Indikator titik pada icon Filter muncul hanya saat Filter ter-Apply

14. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
15. Verifikasi icon Filter tanpa badge titik
16. Klik icon Filter, pilih Event Type `Damaged Repaired`, lalu klik `[Apply]`
17. Klik di luar panel (menutup Filter Panel)
18. Verifikasi badge titik tampil pada icon Filter walau panel tertutup

### TC-FA-NOTIF-427: Filter Panel ditutup lewat klik ulang icon Filter membuang draft

19. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
20. Catat judul item teratas list dan jumlah item yang termuat (baseline)
21. Klik icon Filter, centang `Damaged Repaired`
22. Klik icon Filter lagi sehingga panel menutup
23. Klik icon Filter lagi sehingga panel membuka
24. Verifikasi panel menampilkan nilai ter-Apply terakhir (kosong)
25. Verifikasi judul item teratas dan jumlah item yang termuat sama dengan baseline langkah 20 (list tidak berubah)
26. Verifikasi badge titik tidak muncul pada icon Filter
27. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 9, 14, 19, 27 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 17 (menutup Filter Panel sesudah `[Apply]` tanpa bergantung pada apakah panel menutup otomatis).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 dan 7, 20 dan 25 (baseline dan perbandingan untuk klausa "tabel/list tidak berubah"), langkah 15 (keadaan awal tanpa titik, Expected butir a TC-214).
- Temuan untuk QA:
  - TC-209 dan 427 menulis "tabel tidak berubah" untuk modul tanpa tabel; spec membacanya sebagai list Notification Center dengan baseline judul item teratas dan jumlah item yang termuat.
  - TC-214 langkah 3 menulis "tutup panel" tanpa menyebut caranya; spec memakai klik di luar panel.
