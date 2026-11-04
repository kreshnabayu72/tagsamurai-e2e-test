---
id: TC-FA-TDC-E2E-084-cancel-version-dari-modal-versions-back-esc-dan-hasil-cancelled
title: "Cancel Version: Entri dari Modal Versions, Back dan Esc Tidak Membatalkan, serta Hasil Cancelled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-298
  - TC-FA-TDC-299
  - TC-FA-TDC-300
  - TC-FA-TDC-302
coverage:
  web: automated
---

# Cancel Version: Entri dari Modal Versions, Back dan Esc Tidak Membatalkan, serta Hasil Cancelled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`): class `KHS-C1-{runId}-084` (Class Name `Kelompok cancel uji`), Active, Used By 0, versi Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance) dan satu versi Scheduled Effective From Jan 2027 (Useful Life 10, Straight Line dan Declining Balance). Tabel berisi tujuh class seed bawaan dan class itu (8 baris pada satu halaman); baris dibuka tanpa Search.
- Kemampuan teknis: seeding class dengan versi Scheduled lewat API; menekan `Esc`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik link Class Code `KHS-C1-{runId}-084` pada tabel

### TC-FA-TDC-298: Cancel pada baris Scheduled di modal Versions membuka D-10

2. Klik tautan View versions
3. Pada baris "Jan 2027" berstatus "Scheduled" klik `[Cancel]`
4. Verifikasi modal Versions tertutup
5. Verifikasi dialog D-10 terbuka dengan baris "• KHS-C1-{runId}-084 – Kelompok cancel uji", "Effective From Jan 2027", dan "Are you sure you want to cancel this scheduled version?"; tombol `[Back]` dan `[Cancel version]`
6. Klik `[Back]`

### TC-FA-TDC-299: Tombol Back pada D-10 kembali tanpa perubahan

7. Klik `[Cancel scheduled version]` pada Alert
8. Klik `[Back]`
9. Verifikasi dialog D-10 tertutup
10. Verifikasi Drawer Edit tetap terbuka dan Alert masih menampilkan teks "Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance."
11. Verifikasi tidak ada toast

### TC-FA-TDC-300: Esc pada D-10 menutup dialog tanpa membatalkan versi

12. Klik `[Cancel scheduled version]` pada Alert
13. Tekan `Esc`
14. Verifikasi dialog D-10 tertutup
15. Verifikasi tidak ada toast
16. Klik tautan View versions
17. Verifikasi baris "Jan 2027" tetap berstatus "Scheduled"
18. Tutup modal Versions

### TC-FA-TDC-302: Cancel version dari baris modal Versions membatalkan versi pada baris itu

19. Klik tautan View versions
20. Pada baris "Jan 2027" klik `[Cancel]`
21. Pada D-10 klik `[Cancel version]`
22. Verifikasi toast sukses "Success, scheduled version has been cancelled."
23. Klik tautan View versions
24. Verifikasi modal Versions: baris "Jan 2027" berstatus "Cancelled"
25. Tutup modal Versions
26. Verifikasi field Regulation Reference tampil pada Drawer Edit
27. Verifikasi Alert versi Scheduled tidak tampil pada Drawer Edit
28. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 6 (`[Back]` menutup D-10 agar TC-299 mulai dari Drawer dengan Alert), langkah 18 dan 25 (menutup modal Versions), dan langkah 28 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Langkah 17 menjalankan klausa "versi Jan 2027 tetap Scheduled" pada Expected TC-300 lewat modal Versions; langkah 26 adalah anchor positif untuk absence Alert pada langkah 27 (8b.2).
- Versi Jan 2027 dibatalkan di akhir (langkah 21) karena aksi itu mengubah data (S-10); TC-298, 299, 300 dijalankan sebelumnya pada versi yang sama dan tidak mengubahnya.
- Post Condition TC-299 ("tidak ada entri log"), TC-298 tidak punya Post Condition, dan Post Condition TC-302 (entri log L-09) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-09 ada di spec pencatatan log.
- Temuan untuk QA:
  - TC-299 Post Condition a/b dan TC-302 Post Condition (entri L-09) tanpa langkah observasi di TC.
  - TC-300 Expected "versi Jan 2027 tetap Scheduled" tidak menyebut tempat mengamati; spec memakai modal Versions.
  - Class Code `KHS-C1` ditulis tanpa suffix di TC; spec memakai `-{runId}-084` (S-12).
  - Email akun Total Control tidak tertulis di TC.
