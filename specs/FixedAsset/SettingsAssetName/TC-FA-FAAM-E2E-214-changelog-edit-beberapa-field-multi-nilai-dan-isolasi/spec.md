---
id: TC-FA-FAAM-E2E-214-changelog-edit-beberapa-field-multi-nilai-dan-isolasi
title: "Pencatatan Changelog Edit: Beberapa Field Sekaligus, Field Tidak Berubah, dan Urutan Old-New Multi-Nilai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-570
  - TC-FA-FAAM-571
  - TC-FA-FAAM-587
coverage:
  web: automated
---

# Pencatatan Changelog Edit: Beberapa Field Sekaligus, Field Tidak Berubah, dan Urutan Old-New Multi-Nilai

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 24 (UoM `Unit`, `Set`), No. 25 (Label `Fragile`, `Finance`), lisensi addon `Maps` dan `Audit` aktif (lihat Temuan untuk QA).
- Data Dinamis, di-seed lewat API di hook `before`: `Edit Target Item 570 {runId}-214` (Code `ETI570`), `Edit Target Item 571 {runId}-214` (Code `ETI571`), `Edit Target Item 587 {runId}-214` (Code `ETI587`); salinan fixture 13d (Tabel Dinamis No. 47, 48, 52), Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`. Code mengikuti literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama).
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya; membaca jumlah baris hasil Search Changelog sebelum aksi. Changelog adalah audit trail permanen sehingga jumlah diasersi sebagai selisih terhadap baseline atau terhadap nama bersuffix unik (baseline nol).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus tiga Asset Name seed lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-570, 571, 587: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-214`, tekan Enter

### TC-FA-FAAM-570: Edit beberapa field sekaligus

2. Klik `⋯` baris `Edit Target Item 570 {runId}-214` lalu `Edit`
3. Ubah Code menjadi `ETI570-3`
4. Ubah UoM menjadi `Set`
5. Tambahkan Default Label `Fragile`
6. Klik `[Save]`
7. Klik icon Changelog
8. Ketik Search `Edit Target Item 570 {runId}-214`, tekan Enter
9. Verifikasi tepat tiga baris Edit (Field `Code`, `UoM`, `Default Label`)
10. Verifikasi ketiga baris memiliki Date yang sama
11. Verifikasi tidak ada baris ganda (jumlah baris Edit Asset Name ini tetap tiga)
12. Tutup Modal Changelog

### TC-FA-FAAM-571: Field yang tidak berubah tidak menghasilkan entri dan record lain tidak terpengaruh

13. Klik `⋯` baris `Edit Target Item 571 {runId}-214` lalu `Edit`
14. Ubah hanya Code menjadi `ETI571-4`
15. Klik `[Save]`
16. Klik icon Changelog
17. Ketik Search `Edit Target Item 571 {runId}-214`, tekan Enter
18. Verifikasi hanya satu baris Field `Code`
19. Ganti isi kotak search dengan `Edit Target Item 570 {runId}-214`, tekan Enter
20. Verifikasi jumlah baris Edit Asset Name `Edit Target Item 570 {runId}-214` tetap tiga seperti pada langkah 9 (Asset Name lain tidak mendapat entri)
21. Tutup Modal Changelog

### TC-FA-FAAM-587: Old/New multi-nilai memakai urutan enum atau A→Z

22. Klik `⋯` baris `Edit Target Item 587 {runId}-214` lalu `Edit`
23. Tambahkan Default Addon `Maps` lalu `Audit`
24. Tambahkan Default Label `Fragile` lalu `Finance`
25. Klik `[Save]`
26. Klik icon Changelog
27. Ketik Search `Edit Target Item 587 {runId}-214`, tekan Enter
28. Verifikasi baris Field `Default Addon` New `Audit, Maps` (urutan enum)
29. Verifikasi baris Field `Default Label` New `Finance, Fragile` (A→Z), dipisah `, `

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search untuk mempersempit tabel utama ke tiga seed spec ini), langkah 8, 17, 19, 27 (Search di Modal Changelog untuk menemukan entri target pada audit trail permanen; S-12, S-14), dan langkah 12, 21 (menutup Modal Changelog).
- Pembagian TC lintas spec: Expected TC-FA-FAAM-570 butir b dan TC-FA-FAAM-571 butir b memuat klausa "tidak ada baris untuk field yang tidak berubah" dan "Asset Name lain tidak mendapat entri". Spec ini mengasersinya sebagai jumlah (langkah 11 dan 20) dengan anchor baris yang ada; asersi absence murni (S-05) tidak ditulis di spec fungsional ini. Lihat Temuan untuk QA.
- Temuan untuk QA:
  - TC-FA-FAAM-571 butir b (dan TC-FA-FAAM-570 butir b) berisi klausa absence log tanpa spec kelas g yang memuat aksi nyata untuk TC ini (spec 216 hanya memuat TC-FA-FAAM-588 untuk pola serupa). Spec ini menutupnya dengan asersi jumlah; keputusan pemilik: pindahkan klausa absence ke spec 216 atau terima asersi jumlah.
  - TC-FA-FAAM-587 menambah Default Addon `Maps`, sementara Pre-setup No. 10b menyatakan lisensi `Maps` tidak teralokasi aktif pada client Automation; precondition TC kurang. Spec mengasumsikan lisensi `Maps` dan `Audit` aktif (disediakan tim FE/BE).
  - TC-FA-FAAM-570 menyebut "Date sama" tanpa batas toleransi; kolom Date log berketelitian menit.
