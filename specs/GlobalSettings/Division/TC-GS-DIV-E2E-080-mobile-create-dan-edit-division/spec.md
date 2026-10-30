---
id: TC-GS-DIV-E2E-080-mobile-create-dan-edit-division
title: "Mobile: Create dan Edit Division"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-285
  - TC-GS-DIV-286
coverage:
  mobile: automated
---

# Mobile: Create dan Edit Division

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji bersama, sehingga suite berjalan serial (`parallel: false`, S-09).
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini pada aplikasi Android; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat spec lewat UI mobile: `Mobile Unit {runId}-080` dengan Code `MBL` (D-20; Code `MBL` dipakai sesuai TC), lalu diubah menjadi `Mobile Unit 2 {runId}-080`. Spec tidak memakai Division Pre-setup atau Population.
- Cleanup (hook `after`, tidak berasumsi langkah spec berhasil penuh): hapus lewat API `Mobile Unit {runId}-080` dan `Mobile Unit 2 {runId}-080` bila ada (kemampuan menghapus Division lewat API). Hook `before` menghapus lewat API sisa Division bernama `Mobile Unit *-080` dan `Mobile Unit 2 *-080` yang masih memegang Code `MBL` (bukan berdasarkan Code saja).
- Kemampuan teknis: gesture tap, input teks, dan pembukaan bottom sheet di perangkat atau emulator Android.
- Tidak ada state global yang diubah.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- TC-GS-DIV-285 dan 286: aplikasi TAG Samurai Mobile (Android) terbuka sebagai Total Control.

## Test Steps

### TC-GS-DIV-285: Create Division dari mobile berhasil

1. Ketuk `[+ Division]`
2. Isi Division Name `Mobile Unit {runId}-080` dan Code `MBL`
3. Ketuk [Submit]
4. Verifikasi toast sukses: `Success, division has been created.`
5. Ketuk icon `[🔍]` pada toolbar, lalu cari `Mobile Unit {runId}-080`
6. Verifikasi card `Mobile Unit {runId}-080` tampil pada card list

### TC-GS-DIV-286: Edit Division dari mobile tampil sebagai bottom sheet dan berhasil disimpan

7. Ketuk `[⋯]` pada card `Mobile Unit {runId}-080`, lalu ketuk `Edit`
8. Verifikasi form Edit Division tampil sebagai bottom sheet
9. Verifikasi Division Name terisi `Mobile Unit {runId}-080`
10. Verifikasi Code terisi `MBL`
11. Ubah Division Name menjadi `Mobile Unit 2 {runId}-080`
12. Ketuk [Save]
13. Verifikasi toast sukses: `Success, division has been updated.`
14. Cari `Mobile Unit 2 {runId}-080` pada inline search (menggantikan pencarian sebelumnya)
15. Verifikasi card menampilkan `Mobile Unit 2 {runId}-080`
16. Hapus isi inline search

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Spec mobile Android (`coverage.mobile: automated`, tanpa `web`, mengikuti spec mobile suite Brand). Platform mobile (Android), satu akun; tidak termasuk kelas harness prinsip 13.
- Urutan TC sama dengan urutan sumber (285 lalu 286); Division yang dibuat pada TC-GS-DIV-285 dipakai TC-GS-DIV-286 di spec yang sama, tidak menumpang spec lain.
- Langkah penghubung: langkah 5, 14, dan 16 (inline search nama Division uji supaya card berada di layar, lalu mengosongkannya); langkah 5 tidak ada di Langkah Uji TC.
- Expected Result a TC-GS-DIV-286 dipecah menjadi langkah 8 (bottom sheet), 9 (Division Name terisi), dan 10 (Code terisi) sesuai S-01.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-285 dan 286: TC tidak menyebut apakah bottom sheet Create atau Edit menutup otomatis setelah sukses; spec tidak mengasersi dan tidak menambah langkah menutup form. Nilai Name pada langkah 11 menggantikan isian lama; TC tidak menyebut cara mengosongkan field.
  - TC-GS-DIV-285 dan 286: TC memakai Name literal `Mobile Unit` dan `Mobile Unit 2`; spec memberi suffix per run (S-12) sehingga asersi memakai nama bersuffix.
  - TC-GS-DIV-285: Post Condition `Division Mobile Unit tersimpan (D-20)` dan TC-GS-DIV-286 `Name Mobile Unit menjadi Mobile Unit 2` tidak punya langkah observasi tambahan di luar Expected Result dan tidak diasersi terpisah.
