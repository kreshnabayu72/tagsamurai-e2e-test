---
id: TC-AC-PF-E2E-016-konkurensi-retry-delete-plan-name-diklik-setelah-plan-dihapus-sesi-lain
title: "Konkurensi Delete: Retry Delete Custom dan Default Plan serta Plan Name Diklik Setelah Plan Dihapus Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-595
  - TC-AC-PF-596
  - TC-AC-PF-781
coverage:
  web: automated
---

# Konkurensi Delete: Retry Delete Custom dan Default Plan serta Plan Name Diklik Setelah Plan Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor pertama): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun sesi B (konteks browser kedua): Total Control Principal kedua `secondAdminPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`, Pre-setup #9), password dari `Spectra.env.AC_PF_SA_PASSWORD`. Kelas harness: c multi-konteks (dua sesi UI; sesi B menjadi objek asersi).
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Sesi B login pada langkah 1 di konteks browser kedua; hook `after` menutup konteks kedua dan mengembalikan sesi ke akun default suite.
- Data milik spec (hook `before`, dibuat lewat fixture BE, dibersihkan di hook `after`): tiga plan archived Clients 0 yang tidak pernah dipakai dan bersuffix, mengikuti bentuk Dataset Plan C dan Dataset Plan R: custom plan `Arsip Custom Satu {runId}-016` (TC-AC-PF-595), default plan `Plan Arsip Lama {runId}-016` (TC-AC-PF-596), custom plan `Arsip Custom Tiga {runId}-016` (TC-AC-PF-781). Plan dihapus permanen oleh aksi spec; hook `after` membersihkan sisa lewat fixture BE. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: konteks browser kedua dengan login akun #9; fixture BE (pembuatan dan pembersihan plan archived) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: entri Changelog Delete bersifat permanen dan tidak dapat dihapus lewat UI.
- Env var: `Spectra.env.AC_TC_PASSWORD` (sesi A) dan `Spectra.env.AC_PF_SA_PASSWORD` (sesi B); nama `AC_PF_SA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-595: Retry Delete pada custom plan yang sudah terhapus: plan tidak ditemukan dan daftar disegarkan dengan toast netral

1. Sesi B: buka konteks browser kedua, login sebagai Total Control kedua (Principal), buka Plans & Licensing > Plans & Features, klik tab Custom, klik sub-tab Archive, ketik Search `Arsip Custom Satu {runId}-016`, tekan Enter
2. Sesi A: klik tab Custom, klik sub-tab Archive, ketik Search `Arsip Custom Satu {runId}-016`, tekan Enter
3. Sesi A: buka Overlay Row Action `Arsip Custom Satu {runId}-016`, klik `Delete` sehingga dialog `Delete Plan` terbuka
4. Sesi B: buka Overlay Row Action `Arsip Custom Satu {runId}-016`, klik `Delete` sehingga dialog `Delete Plan` terbuka
5. Sesi A: klik `[Delete]`
6. Verifikasi sesi A menampilkan toast sukses: "Success, plan has been permanently deleted."
7. Sesi B: klik `[Delete]`
8. Verifikasi sesi B menampilkan toast netral: "This plan is no longer available."
9. Verifikasi daftar sesi B disegarkan dan `Arsip Custom Satu {runId}-016` tidak ada lagi di sub-tab Archive
10. Verifikasi sesi B tidak menampilkan toast error
11. Sesi A: klik ikon Changelog pada toolbar tab Custom
12. Verifikasi modal Changelog Custom menampilkan entri Delete untuk `Arsip Custom Satu {runId}-016`
13. Verifikasi Changelog memuat tepat satu entri Delete untuk `Arsip Custom Satu {runId}-016`
14. Tutup modal Changelog lewat `✕`
15. Sesi A: klik `(←)` pada kotak Search

### TC-AC-PF-596: Retry Delete pada default plan yang sudah terhapus: plan tidak ditemukan dan daftar disegarkan dengan toast netral

16. Sesi A: klik tab Default, klik sub-tab Archive, ketik Search `Plan Arsip Lama {runId}-016`, tekan Enter
17. Sesi B: klik tab Default, klik sub-tab Archive, ketik Search `Plan Arsip Lama {runId}-016`, tekan Enter
18. Sesi A: buka Overlay Row Action `Plan Arsip Lama {runId}-016`, klik `Delete` sehingga dialog `Delete Plan` terbuka
19. Sesi B: buka Overlay Row Action `Plan Arsip Lama {runId}-016`, klik `Delete` sehingga dialog `Delete Plan` terbuka
20. Sesi A: klik `[Delete]`
21. Verifikasi sesi A menampilkan toast sukses: "Success, plan has been permanently deleted."
22. Sesi B: klik `[Delete]`
23. Verifikasi sesi B menampilkan toast netral: "This plan is no longer available."
24. Verifikasi daftar sesi B disegarkan dan `Plan Arsip Lama {runId}-016` tidak ada lagi di sub-tab Archive
25. Verifikasi sesi B tidak menampilkan toast error
26. Sesi A: klik ikon Changelog pada toolbar tab Default
27. Verifikasi modal Changelog Default menampilkan entri Delete untuk `Plan Arsip Lama {runId}-016`
28. Verifikasi Changelog memuat tepat satu entri Delete untuk `Plan Arsip Lama {runId}-016`
29. Tutup modal Changelog lewat `✕`
30. Sesi A: klik `(←)` pada kotak Search

### TC-AC-PF-781: Plan Name diklik setelah plan dihapus sesi lain: toast netral, Plan Detail tidak terbuka, dan daftar disegarkan

31. Sesi A dan sesi B: klik tab Custom, klik sub-tab Archive, ketik Search `Arsip Custom Tiga {runId}-016`, tekan Enter
32. Sesi B: buka Overlay Row Action `Arsip Custom Tiga {runId}-016`, klik `Delete`, lalu klik `[Delete]` pada dialog `Delete Plan`
33. Verifikasi sesi B menampilkan toast sukses: "Success, plan has been permanently deleted."
34. Sesi A: tanpa menyegarkan halaman, klik teks `Arsip Custom Tiga {runId}-016` pada kolom Plan Name
35. Verifikasi sesi A menampilkan toast netral: "This plan is no longer available."
36. Verifikasi sesi A tidak menampilkan dialog error
37. Verifikasi sesi A tetap di list Plans & Licensing > Plans & Features > Custom > Archive (Plan Detail tidak terbuka)
38. Verifikasi daftar sesi A disegarkan dan `Arsip Custom Tiga {runId}-016` tidak ada lagi

## Notes

- P-1: asersi `tepat satu entri Delete` pada langkah 13 dan 28 dan asersi tanpa toast error pada langkah 10 dan 25 bergantung pada state dua sesi yang baru dibangun langkah sebelumnya (kedua dialog `Delete Plan` terbuka sebelum Delete pertama); baseline berupa nama plan bersuffix (baseline nol) dengan anchor positif langkah 12 dan 27 (S-12, bagian 8b butir 2).
- Langkah penghubung (S-03): klik tab, sub-tab, dan Search pada langkah 1, 2, 16, 17, dan 31 mengarahkan layar ke tab yang disyaratkan precondition TC dan menemukan baris target (R-16); langkah 14 dan 29 menutup modal; langkah 15 dan 30 mengosongkan Search.
- Plan uji memakai nama bersuffix (S-12) sebagai ganti `Arsip Custom Satu` (Dataset Plan C) dan `Plan Arsip Lama` (Dataset Plan R); tiap blok memakai plan sendiri karena plan dihapus permanen (S-06).
- Alasan di atas sekitar 35 langkah (38 langkah): ketiga blok satu kelas harness (c multi-konteks, plan dihapus sesi lain) dan satu topik (konflik Delete), tiap blok memakai plan sendiri dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-PF-595 dan TC-AC-PF-596: Expected b menyebut "server menjawab plan tidak ditemukan (`Plan not found`)"; jawaban server tidak terlihat di UI dan tidak diasersi, hanya toast netral, daftar yang disegarkan, dan tidak adanya toast error yang teramati.
