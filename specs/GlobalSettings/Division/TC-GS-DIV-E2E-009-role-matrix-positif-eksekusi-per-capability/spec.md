---
id: TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-26
  - TC-GS-DIV-27
  - TC-GS-DIV-28
  - TC-GS-DIV-29
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun | Nama user | Env var password | Aksi yang dieksekusi |
|---|---|---|---|---|
| System Role: Create dan Read | `createOnly_automated_qaTeam1@qwertysystem.net` | Rina Marlina | `Spectra.env.GS_CREATE_PASSWORD` | Create (TC-GS-DIV-26) |
| System Role: Update dan Read | `updateOnly_automated_qaTeam1@qwertysystem.net` | Agus Wijaya | `Spectra.env.GS_UPDATE_PASSWORD` | Update (TC-GS-DIV-27) |
| System Role: Delete dan Read | `deleteOnly_automated_qaTeam1@qwertysystem.net` | Dewi Lestari | `Spectra.env.GS_DELETE_PASSWORD` | Delete dan Bulk Delete (TC-GS-DIV-28, TC-GS-DIV-29) |

- Login akun Create dan Read (aktor pertama spec) dilakukan di hook `before`; Update dan Read serta Delete dan Read memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Delete dan Read, hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, dan `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Dinamis (suffix per run ditambah nomor spec `{runId}-009`; Code di-generate otomatis, tidak diasersi):
  - `Corporate Secretary {runId}-009` (D-01): dibuat lewat UI di TC-GS-DIV-26 dengan Code dikosongkan, diubah menjadi `Corporate Secretariat {runId}-009` di TC-GS-DIV-27, dihapus di TC-GS-DIV-28 (rantai TC dalam spec yang sama; tidak menumpang spec lain).
  - `Internal Affairs {runId}-009` dan `Investor Relations {runId}-009`: Division bebas relasi, di-seed lewat kemampuan "seeding Division lewat API" di hook `before` (padanan TC-GS-DIV-36 dan TC-GS-DIV-66 yang menjadi dependensi TC-GS-DIV-29), dihapus di TC-GS-DIV-29.
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API Division `Corporate Secretary {runId}-009`, `Corporate Secretariat {runId}-009`, `Internal Affairs {runId}-009`, dan `Investor Relations {runId}-009` bila masih ada, lalu pulihkan sesi ke akun default suite.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-division` untuk ketiga akun lalu menyetelnya ke true supaya walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal tiap akun. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- Kemampuan teknis: logout dan login ulang dengan akun berbeda dalam satu spec; seeding dan cleanup Division lewat API. Master Data Count Limit dan Selection Limit tidak diubah (nilai bawaan environment).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-DIV-26: Aktor Create-saja berhasil membuat Division

1. Klik `[+ Division]`
2. Isi Division Name `Corporate Secretary {runId}-009`
3. Biarkan Code kosong
4. Klik `[Submit]`
5. Verifikasi modal Create Division tertutup
6. Verifikasi toast sukses `Success, division has been created.`
7. Ketik Search `{runId}-009`, tekan Enter
8. Verifikasi baris `Corporate Secretary {runId}-009` tampil di tabel

### TC-GS-DIV-27: Aktor Update-saja berhasil mengubah Name Division

9. Logout, lalu login sebagai System Role: Update dan Read
10. Buka Global Settings > User > Tab Division
11. Ketik Search `{runId}-009`, tekan Enter
12. Buka row action baris `Corporate Secretary {runId}-009` lalu klik `Edit`
13. Ubah Division Name menjadi `Corporate Secretariat {runId}-009`
14. Klik `[Save]`
15. Verifikasi modal Edit Division tertutup
16. Verifikasi toast sukses `Success, division has been updated.`
17. Verifikasi baris tabel menampilkan `Corporate Secretariat {runId}-009`

### TC-GS-DIV-28: Aktor Delete-saja berhasil menghapus Division bebas relasi

18. Logout, lalu login sebagai System Role: Delete dan Read
19. Buka Global Settings > User > Tab Division
20. Ketik Search `{runId}-009`, tekan Enter
21. Buka row action baris `Corporate Secretariat {runId}-009` lalu klik `Delete`
22. Klik `[Delete]` pada dialog konfirmasi
23. Verifikasi dialog `Delete Division` tertutup
24. Verifikasi toast sukses `Success, division has been deleted.`
25. Verifikasi baris `Corporate Secretariat {runId}-009` hilang dari tabel

### TC-GS-DIV-29: Aktor Delete-saja berhasil menjalankan Bulk Delete

26. Centang baris `Internal Affairs {runId}-009` dan `Investor Relations {runId}-009`
27. Klik aksi `[Delete]` pada Bulk Action Bar
28. Verifikasi dialog `Delete Division` tampil
29. Verifikasi dialog memuat bullet `Internal Affairs {runId}-009` dan `Investor Relations {runId}-009`
30. Klik `[Delete]` pada dialog konfirmasi
31. Verifikasi toast sukses `Success, division has been deleted.`
32. Verifikasi baris `Internal Affairs {runId}-009` dan `Investor Relations {runId}-009` hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan karena TC-GS-DIV-27 dan TC-GS-DIV-28 bergantung pada hasil TC sebelumnya (kolom Dependensi) dan aksi Delete memang paling akhir; rantai ini ada di dalam satu spec sehingga spec tetap bisa jalan sendiri.
- Search `{runId}-009` (langkah 7, 11, 20) dipakai di TC-GS-DIV-26 sampai TC-GS-DIV-28 agar Division milik spec ini tampil di halaman aktif sebelum diverifikasi atau dipilih; TC-GS-DIV-29 melanjutkan hasil Search `{runId}-009` yang masih aktif pada akun Delete dan Read (tabel ter-refresh dengan filter aktif setelah Delete, sehingga `Internal Affairs {runId}-009` dan `Investor Relations {runId}-009` sudah tampil tanpa Search ulang), karena jumlah baris tabel bergantung pada Population D-02 yang mungkin ada; ini hanya cara menemukan baris, bukan bagian dari asersi TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 18 (ganti akun) serta langkah 7, 11, dan 20 (Search `{runId}-009`).
- Nama Division memakai suffix `{runId}-009` karena nama Corporate Secretary/Secretariat, Internal Affairs, dan Investor Relations juga dipakai spec lain; TC sumber memakai nama tanpa suffix.
- Temuan untuk QA:
  - TC-GS-DIV-28 dan TC-GS-DIV-27 menyebut Division `Corporate Secretary` dan `Corporate Secretariat` bernama literal; spec menambah suffix per run sehingga nama pada Expected Result TC diganti dengan nama bersuffix.
  - TC-GS-DIV-29 precondition menyebut `Internal Affairs` dan `Investor Relations` dari TC-GS-DIV-36 dan TC-GS-DIV-66 dengan Code `IAF` dan `INV`; spec men-seed lewat API dengan Code di-generate otomatis karena Code `IAF` dan `INV` juga dibuat TC-GS-DIV-36 dan TC-GS-DIV-66 (Tabel Data Uji Dinamis D-05 dan D-11) dan Code harus unik.
