---
id: TC-GS-DIV-E2E-066-modified-by-aktor-pelaksana-tiap-aksi
title: "Pencatatan Changelog: Modified By Mencatat Aktor Pelaksana"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-246
coverage:
  web: automated
---

# Pencatatan Changelog: Modified By Mencatat Aktor Pelaksana

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai empat akun UI berurutan dan berganti akun secara eksplisit; Tabel Data Uji Pre-setup baris 4, 5, 6, dan 1):

  | Urutan | Role | Nama | Email | Environment variable password |
  |---|---|---|---|---|
  | 1 | System Role: Create dan Read | Rina Marlina (`Rina M`) | `createOnly_automated_qaTeam1@qwertysystem.net` | `GS_CREATE_PASSWORD` |
  | 2 | System Role: Update dan Read | Agus Wijaya (`Agus W`) | `updateOnly_automated_qaTeam1@qwertysystem.net` | `GS_UPDATE_PASSWORD` |
  | 3 | System Role: Delete dan Read | Dewi Lestari (`Dewi L`) | `deleteOnly_automated_qaTeam1@qwertysystem.net` | `GS_DELETE_PASSWORD` |
  | 4 | Total Control | Sari Dewi (`Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun 4). Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: logout dan login ulang dalam satu spec (ganti akun); penghapusan Division lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`) untuk cleanup.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): Division `Corporate Secretary {runId}-066` (D-01) dengan Code dikosongkan; dibuat spec oleh akun 1 pada langkah 1 (setara dependensi TC-GS-DIV-26), di-rename menjadi `Corporate Secretariat {runId}-066` oleh akun 2 (setara dependensi TC-GS-DIV-27), lalu dihapus oleh akun 3 (setara dependensi TC-GS-DIV-28). Ketiga aksi memang objek tiga entri Changelog yang dibaca TC-GS-DIV-246.
- Cleanup (hook `after`, tidak berasumsi langkah berhasil penuh): hapus lewat API `Corporate Secretary {runId}-066` dan `Corporate Secretariat {runId}-066` bila masih ada. Entri Changelog bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Tidak ada state global yang diubah.
- TC-GS-DIV-246: login sebagai Total Control dan berada di Global Settings > User > Division, setelah aksi Create-only, Update-only, dan Delete-only dijalankan (dependensi TC-GS-DIV-26, 27, 28).

## Test Steps

### Dependensi TC-GS-DIV-26, 27, 28: aksi per capability

1. Klik [+ Division], isi Division Name `Corporate Secretary {runId}-066`, biarkan Code kosong, klik [Submit]
2. Tunggu aksi selesai (modal Create tertutup)
3. Logout, lalu login sebagai Update-only (`updateOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_UPDATE_PASSWORD`
4. Buka Global Settings > User > Division, ketik Search `Corporate Secretary {runId}-066`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Corporate Secretariat {runId}-066`, klik [Save]
5. Tunggu aksi selesai (modal Edit tertutup)
6. Logout, lalu login sebagai Delete-only (`deleteOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_DELETE_PASSWORD`
7. Buka Global Settings > User > Division, ketik Search `Corporate Secretariat {runId}-066`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog konfirmasi
8. Tunggu aksi selesai (dialog konfirmasi Delete tertutup)
9. Logout, lalu login sebagai Total Control (`totalControl_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`

### TC-GS-DIV-246: Modified By mencatat aktor pelaksana tiap aksi

10. Buka Global Settings > User > Division, buka Modal Changelog, ketik Search `{runId}-066`, tekan Enter
11. Verifikasi Changelog: entri Create `Corporate Secretary {runId}-066` memiliki Modified By `Rina M`
12. Verifikasi Changelog: entri Edit `Corporate Secretariat {runId}-066` memiliki Modified By `Agus W`
13. Verifikasi Changelog: entri Delete `Corporate Secretariat {runId}-066` memiliki Modified By `Dewi L`
14. Hover Modified By `Rina M` pada entri Create
15. Verifikasi tooltip Modified By entri Create: `Rina Marlina`
16. Hover Modified By `Agus W` pada entri Edit
17. Verifikasi tooltip Modified By entri Edit: `Agus Wijaya`
18. Hover Modified By `Dewi L` pada entri Delete
19. Verifikasi tooltip Modified By entri Delete: `Dewi Lestari`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Dependensi TC-GS-DIV-26, 27, 28 dijalankan sebagai langkah 1 sampai 8 di spec ini (S-04), dengan Division milik spec bersuffix `{runId}-066`, bukan bergantung pada spec lain. Hasil ketiga aksi itu (modal tertutup, toast sukses, baris tampil atau hilang) tidak diasersi di sini karena bukan Expected Result TC-GS-DIV-246; diasersi di spec `TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability`.
- Spec ini memakai empat akun berurutan dengan langkah ganti akun eksplisit (langkah 3, 6, dan 9); akun aktor pertama login di hook `before` dan sesi dipulihkan ke akun default suite di hook `after`.
- Entri dikenali lewat nama bersuffix `{runId}-066`; entri milik run lain diabaikan. Search `{runId}-066` pada langkah 10 menampilkan tiga entri hasil langkah 1, 4, dan 7.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search nama Division pada tabel Division sebelum Edit dan Delete (langkah 4 dan 7), buka Global Settings > User > Division (langkah 4, 7, dan 10), serta langkah 2, 5, dan 8 (menunggu aksi selesai sebelum `Logout` pada langkah 3, 6, dan 9, supaya request tidak terputus sebelum entri Changelog tercatat; 8b butir 8). Search tidak tertulis di Langkah Uji TC sumber karena tabel A-Z memiliki lebih dari satu halaman.
- Langkah 11 sampai 13 memverifikasi teks Modified By, langkah 15, 17, dan 19 tooltip; Expected Result a, b, dan c masing-masing berisi dua klausa (teks sel dan tooltip) sehingga dipisah (S-01). Tooltip diasersi sesudah hover pada langkah 14, 16, dan 18 sebelum hover berikutnya mengubah state tooltip.
- Temuan untuk QA: TC-GS-DIV-246 Precondition c ("TC eksekusi per capability sudah dijalankan") tidak menyatakan Division mana yang dipakai dan akun mana yang menjalankan; spec menjalankan ulang ketiga aksi dengan Division bersuffix milik sendiri.
