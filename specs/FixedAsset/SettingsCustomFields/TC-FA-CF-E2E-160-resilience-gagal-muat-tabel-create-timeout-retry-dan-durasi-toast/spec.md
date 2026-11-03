---
id: TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast
title: "Resilience: Gagal Muat Tabel, Create Timeout, Retry, dan Durasi Toast"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-22
  - TC-FA-CF-185
  - TC-FA-CF-202
  - TC-FA-CF-609
coverage:
  web: automated
---

# Resilience: Gagal Muat Tabel, Create Timeout, Retry, dan Durasi Toast

## Prerequisites

- Mode: FE+BE (backend nyata). Respons 500 dan timeout dipaksa lewat intercept parsial di atas backend nyata (Pre-setup #26); state backend (field tersimpan atau tidak) tetap diasersi.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis (bersuffix, S-12): `Fail Timeout {runId}-160`, `Retry Item {runId}-160`, `Toast Time {runId}-160`, dan `Toast Err {runId}-160`. Cleanup di hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-160`.
- Kemampuan teknis: intercept dan penundaan respons (`Spectra.intercept`) untuk request daftar custom field dan request Create; pengukuran durasi toast (sekitar 4 detik) dan jeda 10 detik (jeda nyata pendek, di bawah 30 detik).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah; intercept dilepas segera setelah pemicu (S-09). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-22: gagal memuat data tabel

1. Intersep request daftar custom field dengan respons 500
2. Buka Fixed Asset > Settings > Custom Fields (muat ulang halaman)
3. Verifikasi alert error `Unable to load this data.` dengan tombol `[Try Again]` tampil
4. Verifikasi empty state tidak tampil
5. Lepas intersepsi
6. Klik `[Try Again]`
7. Verifikasi data tabel tampil normal

### TC-FA-CF-185: Create timeout

8. Klik `[+ Custom Field]`
9. Isi Field Name `Fail Timeout {runId}-160` dan Data Type `Text`
10. Tunda respons Create melewati batas waktu
11. Klik `[Submit]`
12. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
13. Verifikasi modal tetap terbuka dengan input dipertahankan
14. Verifikasi `[Submit]` aktif kembali
15. Lepas tahanan respons
16. Tutup toast error

### TC-FA-CF-609: retry manual setelah timeout Create

17. Ganti isi Field Name dengan `Retry Item {runId}-160` (Data Type `Text` tetap)
18. Tunda respons Create sampai timeout
19. Klik `[Submit]`
20. Verifikasi toast `Connection problem. Please try again.` tampil pada percobaan pertama
21. Lepas tahanan respons
22. Klik `[Submit]` lagi tanpa penundaan
23. Verifikasi retry sukses dengan toast `Success, custom field has been created.`
24. Ketik Search `Retry Item {runId}-160`, tekan Enter
25. Verifikasi tepat satu baris `Retry Item {runId}-160` tersimpan
26. Klik `(←)` pada kotak Search

### TC-FA-CF-202: durasi toast sukses dan toast error

27. Klik `[+ Custom Field]`
28. Tunggu toast lama hilang otomatis
29. Isi Field Name `Toast Time {runId}-160` dan Data Type `Text`, klik `[Submit]`, dan ukur waktu toast sukses
30. Verifikasi toast `Success, custom field has been created.` hilang otomatis sekitar 4 detik
31. Klik `[+ Custom Field]`
32. Isi Field Name `Toast Err {runId}-160` dan Data Type `Text`
33. Intersep respons Create dengan 500
34. Klik `[Submit]`
35. Tunggu 10 detik
36. Verifikasi toast `Error, failed to create custom field.` tetap tampil sampai di-dismiss manual
37. Klik `[Submit]` lagi (intersepsi tetap aktif)
38. Verifikasi toast error baru menggantikan toast yang sedang tampil
39. Lepas intersepsi
40. Tutup toast error
41. Klik icon close `[✕]`
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 43 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas b, fault injection pada alur Create dan muat tabel), berdiri sendiri, dan tiap TC menuntut Verifikasi per klausa (S-01) dan penutupan form dirty yang deterministik (S-08). Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Intercept dipakai sebagai pemicu dan dilepas segera setelah pemicu (S-09); `P-2` tidak diperlukan karena spec ini kelas b.
- TC-FA-CF-185 dan TC-FA-CF-609 memakai modal Create yang sama: modal dibiarkan terbuka dengan input dipertahankan sesudah timeout (Expected TC-FA-CF-185), lalu Field Name diganti pada langkah 17 sehingga tidak ada pembukaan form tambahan (bagian 3, halaman yang dipakai berulang). Toast error dari TC-FA-CF-185 ditutup pada langkah 16 sebelum asersi toast berikutnya (R-12).
- S-05: TC-FA-CF-184 (Create gagal 5xx, termasuk klausa "tidak ada entri log") diasersi di spec 179; spec ini tidak memuat asersi log.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 15, 21, dan 39 (melepas intersepsi), langkah 16 dan 40 (menutup toast), langkah 41 sampai 43 (menutup form dirty, S-08), langkah 35 (jeda nyata pendek di bawah 30 detik, bagian 6).
- Langkah penghubung toast (S-03, R-22): langkah 28 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-202 menyebut "ukur waktu toast sukses" tanpa toleransi; spec mengasersi "sekitar 4 detik" sesuai Expected. Pengukuran dan penanganan toast yang menggantikan toast lama bergantung kemampuan teknis tim FE.
  - TC-FA-CF-609 tidak menyebut kondisi "server tidak commit" selain Pre-setup #26; spec mengasersi tepat satu baris `Retry Item {runId}-160` setelah retry.
