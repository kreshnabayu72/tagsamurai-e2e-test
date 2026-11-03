---
id: TC-AC-DC-E2E-062-changelog-search-nilai-pelaku-trim
title: "Modal Changelog Category: Search Kolom Nilai, Modified By, Trim, Tanggal, dan Teks Literal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-158
  - TC-AC-DC-159
  - TC-AC-DC-160
  - TC-AC-DC-161
  - TC-AC-DC-162
coverage:
  web: automated
---

# Modal Changelog Category: Search Kolom Nilai, Modified By, Trim, Tanggal, dan Teks Literal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-158: Search per kelas kolom nilai campuran: Old Value dan New Value

1. Klik ikon Changelog pada header Sidebar Category
2. Ketik Search `Scanner Pro`, tekan Enter
3. Verifikasi tabel menampilkan baris Edit `Scanner Max` dengan Old Value "Scanner Pro"
4. Verifikasi tabel menampilkan baris Edit `Scanner Pro` dengan Category dan New Value "Scanner Pro"
5. Ganti isi kotak search dengan `scanner max`, tekan Enter
6. Verifikasi tabel hanya menampilkan baris Edit `Scanner Max` dengan New Value "Scanner Max" (pencarian case-insensitive)

### TC-AC-DC-159: Search pada kolom Modified By mencocokkan nama pelaku

7. Ganti isi kotak search dengan `maya`, tekan Enter
8. Verifikasi tabel menampilkan 6 baris yang dilakukan Maya P (Delete `Kit Lama Anak`, Delete `Kit Lama`, Create `Tracker Seven`, Edit `Gateway Kit Plus`, Create `Kit Lama Anak`, Create `Kit Lama`)
9. Verifikasi baris Budi S tidak tampil

### TC-AC-DC-160: Spasi di awal dan akhir kata kunci Search di-trim tanpa mengubah isi kotak pencarian

10. Ganti isi kotak search dengan `  scan  ` (spasi di awal dan akhir), tekan Enter
11. Verifikasi tabel menampilkan 3 baris yang sama dengan pencarian "scan"
12. Verifikasi isi kotak pencarian di layar tetap `  scan  ` tanpa perubahan

### TC-AC-DC-161: Kolom Date tidak masuk cakupan Search

13. Ganti isi kotak search dengan `sep`, tekan Enter
14. Verifikasi tidak ada baris yang cocok untuk kata kunci "sep" karena nilai tanggal tidak dicari lewat Search
15. Ganti isi kotak search dengan `18/09`, tekan Enter
16. Verifikasi tidak ada baris yang cocok untuk kata kunci "18/09" karena nilai tanggal tidak dicari lewat Search
17. Klik ikon Filter
18. Verifikasi Filter Panel menyediakan field Date untuk menyaring berdasarkan tanggal
19. Klik ikon Filter untuk menutup panel

### TC-AC-DC-162: Kata kunci Search dan nilai sel diperlakukan sebagai teks literal

20. Ganti isi kotak search dengan `<img src=x onerror=alert(1)>`, tekan Enter
21. Verifikasi tidak ada baris yang cocok
22. Verifikasi tidak ada skrip yang tereksekusi (tidak ada dialog alert)
23. Verifikasi kata kunci tidak diinterpretasi sebagai pola pencarian khusus atau markup (kotak pencarian menampilkan teks literal dan tidak ada elemen `<img>` di modal)

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-158, 159, 160, 161, 162). Tidak ada TC hanya-BE di spec ini.
- Absence pada TC-AC-DC-159, 161, dan 162 memakai anchor positif: hasil pencarian sebelumnya (baris tampil pada tabel yang sama) sudah diverifikasi di langkah sebelumnya, atau baris lain pada hasil yang sama (8b.2).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 19.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-161 butir b ('penyaringan tanggal hanya lewat Filter Panel') bukan perilaku yang dapat diamati langsung; spec memverifikasi bahwa Filter Panel menyediakan field Date.
  - TC-AC-DC-162 menyebut 'nilai sel diperlakukan sebagai teks literal' pada judul tanpa Expected terpisah dan tanpa data Changelog bermarkup; spec hanya mengasersi kata kunci Search.
