---
id: TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul
title: "Formula Lintas Modul: #ERROR, Presedensi, dan Evaluasi Saat Dibaca"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-540
  - TC-FA-CF-541
  - TC-FA-CF-542
  - TC-FA-CF-543
coverage:
  web: automated
---

# Formula Lintas Modul: #ERROR, Presedensi, dan Evaluasi Saat Dibaca

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Aset konsumen A1 (Asset Name `Pump`, Active, Purchase Price `100`) dan A2 (Asset Name `Generator`, Active, Purchase Price kosong lalu `1` sesuai TC-FA-CF-542) (Pre-setup #31). Field Formula uji: `Ratio` (`Purchase Price ÷ 0`), Formula `Purchase Price + 1`, `Purchase Price + 10 × 2`, `Purchase Price − 10 + 5`, `Purchase Price ÷ 8`, dan `Total Cost` (`Purchase Price + 10`); daftar dan nama field dirujuk lewat fixture baru `Fixture.faCustomFields.formulaUji` (disediakan tim FE; nama field selain `Ratio` dan `Total Cost` tidak tertulis di TC).
- Kemampuan teknis (disediakan tim FE/BE): sesi API untuk mengisi Purchase Price aset `A2` dengan `1` dan seed field Formula uji.
- State global: tidak ada. Purchase Price A1 dan A2 serta field Formula uji dipulihkan seed reset Company di hook `before` dan `after`; preferensi kolom Asset List yang tersimpan di browser (kolom field Formula) dihapus hook `after` (kemampuan disediakan tim FE).
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-540: Formula pembagian nol menampilkan #ERROR dengan tooltip Division by zero tanpa memblokir

1. Buka Detail aset `A1` (Purchase Price `100`) pada modul Asset
2. Verifikasi nilai Formula `Ratio` (`Purchase Price ÷ 0`) tampil `#ERROR`
3. Arahkan kursor ke nilai `#ERROR`
4. Verifikasi tooltip `Division by zero` tampil
5. Simpan perubahan lain pada aset `A1` (satu field non-Formula dari fixture `Fixture.faCustomFields.formulaUji`)
6. Verifikasi penyimpanan aset `A1` berjalan (tidak diblokir)

### TC-FA-CF-541: Formula dengan field rujukan belum bernilai menampilkan #ERROR dengan tooltip field rujukan

7. Buka Detail aset `A2` (tanpa Purchase Price)
8. Verifikasi nilai Formula `Purchase Price + 1` tampil `#ERROR`
9. Arahkan kursor ke `#ERROR`
10. Verifikasi tooltip `A referenced field has no value` tampil
11. Buka Asset List dan tampilkan kolom field Formula lewat Column Visibility
12. Arahkan kursor ke `#ERROR` pada baris `A2`
13. Verifikasi tooltip `A referenced field has no value` tampil pada `#ERROR` di tabel aset

### TC-FA-CF-542: Evaluasi Formula mengikuti presedensi operator, kiri ke kanan, dan pembulatan round-half-up dua desimal

14. Isi Purchase Price aset `A2` dengan `1` lewat sesi API hingga tersimpan
15. Buka Detail aset `A1` (Purchase Price `100`) untuk tiga Formula: `Purchase Price + 10 × 2`, `Purchase Price − 10 + 5`, dan `Purchase Price ÷ 8`
16. Verifikasi `Purchase Price + 10 × 2` menampilkan `120` pada A1 (× dievaluasi sebelum +)
17. Verifikasi `Purchase Price − 10 + 5` menampilkan `95` pada A1 (setingkat dari kiri ke kanan)
18. Verifikasi `Purchase Price ÷ 8` menampilkan `12.5` pada A1
19. Buka Detail aset `A2` (Purchase Price `1`)
20. Verifikasi `Purchase Price ÷ 8` menampilkan `0.13` pada A2 (0.125 dibulatkan round-half-up ke 2 desimal)

### TC-FA-CF-543: Nilai Formula dihitung saat dibaca mengikuti perubahan operan

21. Buka Detail aset `A1` (Purchase Price `100`) dan catat nilai Formula `Purchase Price + 10`
22. Verifikasi nilai Formula `Purchase Price + 10` tampil `110`
23. Ubah Purchase Price `A1` menjadi `200` lalu buka Detail aset `A1` lagi
24. Verifikasi nilai Formula `Purchase Price + 10` berubah menjadi `210` tanpa langkah penyimpanan Formula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): Detail aset dan Asset List tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC.
- Urutan TC di spec: 540, 541, 542, 543. TC-FA-CF-543 berjalan terakhir karena mengubah Purchase Price `A1` (nilai evaluasi TC-FA-CF-542 bergantung pada `100`). Purchase Price `A2` kosong pada TC-FA-CF-541 dan `1` pada TC-FA-CF-542 (langkah penghubung pengisian lewat sesi API ditulis "... hingga ... tersimpan", R-20).
- Asersi tooltip transient diletakkan tepat sesudah hover (8b butir 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Purchase Price `A2`, hover, dan pembukaan Detail aset.
- Temuan untuk QA:
  - TC-FA-CF-540 "Simpan perubahan lain pada aset" tidak menyebut field yang diubah; spec memakai satu field non-Formula dari fixture.
  - TC-FA-CF-542 menyebut tiga Formula uji tanpa nama field; spec merujuk ekspresinya dan nama field dari fixture.
  - TC-FA-CF-543 menulis "tanpa langkah penyimpanan Formula" sebagai Expected; spec mengasersi hasil nilai dan tidak punya langkah observasi tersendiri untuk ketiadaan penyimpanan.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
