---
id: TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete
title: "Pencatatan Changelog: Entri Delete dan Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-242
  - TC-GS-DIV-243
coverage:
  web: automated
---

# Pencatatan Changelog: Entri Delete dan Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), semuanya Division bebas relasi milik spec ini yang di-seed lewat API di hook `before` dan dihapus lewat UI pada spec ini:
  - `Log Create Renamed {runId}-065`: dihapus single pada TC-GS-DIV-242 (setara dependensi TC-GS-DIV-238).
  - `Bulk Log A {runId}-065` dan `Bulk Log B {runId}-065`: dihapus lewat Bulk Delete pada TC-GS-DIV-243. Dipakai sebagai pengganti `Business Development` dan `Corporate Communication` (Population D-02, TC-GS-DIV-30) supaya Population yang dipakai spec lain tidak terhapus.
- Kemampuan teknis: seeding Division lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga Division bersuffix `{runId}-065` bila masih ada. Entri Changelog bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Tidak ada state global yang diubah.
- TC-GS-DIV-242 dan 243: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-242: Delete mencatat satu entri Division Name dengan New Value strip

1. Ketik Search `Log Create Renamed {runId}-065`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog konfirmasi
2. Tunggu aksi selesai (dialog konfirmasi Delete tertutup)
3. Buka Modal Changelog, ketik Search `Log Create Renamed {runId}-065`, tekan Enter
4. Verifikasi Changelog: tepat 1 entri dengan Action `Delete`, Division Name `Log Create Renamed {runId}-065`, Field `Division Name`, Old Value `Log Create Renamed {runId}-065`, New Value `—`, Modified By `Sari D`
5. Tutup Modal Changelog, buka Global Settings > Activity Log, ketik Search `Log Create Renamed {runId}-065`, tekan Enter
6. Verifikasi Activity Log: tepat 1 entri dengan Action `Delete`, Object `Division`, Name `Log Create Renamed {runId}-065`

### TC-GS-DIV-243: Bulk Delete mencatat satu entri per Division yang berhasil dihapus

7. Buka Global Settings > User > Division, ketik Search `{runId}-065`, tekan Enter pada tabel Division, centang baris `Bulk Log A {runId}-065` dan `Bulk Log B {runId}-065`
8. Klik aksi [Delete] pada Bulk Action Bar, klik [Delete] pada dialog konfirmasi
9. Tunggu aksi selesai (dialog konfirmasi Delete tertutup)
10. Buka Modal Changelog, ketik Search `Bulk Log`, tekan Enter
11. Verifikasi Changelog: tepat 2 entri `Delete` bersuffix `{runId}-065`, satu per Division: `Bulk Log A {runId}-065` dan `Bulk Log B {runId}-065`
12. Verifikasi Changelog: entri Delete `Bulk Log A {runId}-065` memiliki Old Value `Bulk Log A {runId}-065` dan New Value `—`
13. Verifikasi Changelog: entri Delete `Bulk Log B {runId}-065` memiliki Old Value `Bulk Log B {runId}-065` dan New Value `—`
14. Verifikasi hasil Search `Bulk Log` tidak memuat entri Delete bersuffix `{runId}-065` untuk Division selain `Bulk Log A {runId}-065` dan `Bulk Log B {runId}-065`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Urutan TC di spec: 242 lalu 243, sesuai urutan sumber; keduanya aksi Delete sehingga tidak ada kasus lain yang butuh baris itu tetap ada.
- Dependensi TC-GS-DIV-238 (Division `Log Create Renamed` ada) dan TC-GS-DIV-30 (Division untuk Bulk Delete) dijalankan lewat seeding API di hook `before`, bukan bergantung pada spec lain. Pembuatan dan perubahan Division lewat UI diuji di spec `TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit`.
- Entri log dikenali lewat nama bersuffix `{runId}-065`; entri milik run lain diabaikan. Search Changelog `Bulk Log` pada langkah 10 mengikutsertakan entri run lain, sehingga langkah 11 dan 14 membatasi pada suffix `{runId}-065`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (pindah ke Activity Log), langkah 7 (kembali ke tab Division), langkah 2 dan 9 (menunggu dialog konfirmasi Delete tertutup sebelum aksi berikutnya, 8b butir 8), dan Search `{runId}-065` pada langkah 7 (baris target dicari dulu karena tabel A-Z memiliki lebih dari satu halaman). Dialog konfirmasi Delete pada langkah 1 dan 8 tidak diasersi karena bukan bagian Expected Result TC-GS-DIV-242 dan 243 (dialog diasersi di spec Delete).
- Hasil dua Delete lewat UI (toast sukses, baris hilang dari tabel) tidak diasersi di spec ini karena tidak ada di Expected Result TC sumber.
- Temuan untuk QA:
  - TC-GS-DIV-243 Expected Result b ("Tidak ada entri untuk Division yang di-skip") tidak punya objek: kedua Division terpilih bebas relasi dan tidak ada Division yang di-skip. Spec mengikuti TC dengan memverifikasi tidak ada entri bersuffix selain kedua Division terpilih (langkah 14); asersi skip in-use yang bermakna ada di TC-GS-DIV-244 (spec `TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use`).
  - TC-GS-DIV-242 Expected Result b tidak menyebut kolom Activity Log selain Action dan Object; spec menambahkan Name hasil Search sebagai pengenal entri.
