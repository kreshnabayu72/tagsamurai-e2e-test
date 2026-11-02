---
id: TC-AC-CS-E2E-123-subscription-log-entri-detail-dan-role
title: "Subscription Log: Entri Detail dan Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-591
  - TC-AC-CS-592
coverage:
  web: automated
---

# Subscription Log: Entri Detail dan Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit):

| Urutan | Pre-setup | Email | Peran | Env password |
|---|---|---|---|---|
| 2 | #3 | `readOnlySub_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`) | Read Only, Principal PT ABC | `Spectra.env.AC_SUB_RO_PASSWORD` |
| 3 | #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager scope Group `Jawa` beserta descendant, Distributor PT Maju Bersama | `Spectra.env.AC_SUB_GM_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data Pre-setup (baca-saja): `SUBS-20260101-00001` (#61: Active, Client PT Sejahtera, FAMS, Professional); `SUBS-20260101-00002` (#58: Archive); `SUBS-20250815-00001` (#69: Warung Kopi Senja, group `Jawa`, Active). Baris di luar scope READ Group Manager `Dewi Anggraini` dirujuk lewat `Fixture.license-allocation-subscription.outOfScopeRow` (Subscription ID tidak disebut TC; lihat Temuan untuk QA).
- Spec tidak menulis data. Sesi dikembalikan ke akun default suite (Total Control Principal) oleh hook `after` spec ini.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen` untuk akun UI suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-591: Tombol Subscription Log pada Subscription Detail membuka modal yang sama

1. Ketik Search `SUBS-20260101-00001`, tekan Enter
2. Klik baris `SUBS-20260101-00001`
3. Verifikasi Subscription Detail `SUBS-20260101-00001` term Active memuat tombol Renew, Cancel Subscription, dan Subscription Log di pojok kanan atas card Subscription Info
4. Klik `Subscription Log`
5. Verifikasi modal Subscription Log berisi Subscription ID `SUBS-20260101-00001`
6. Klik `[✕]`
7. Klik menu `Client Subscription` di sidebar, klik tab `History`
8. Ketik Search `SUBS-20260101-00002`, tekan Enter
9. Klik baris `SUBS-20260101-00002`
10. Verifikasi Subscription Detail term Archive memuat tombol Subscription Log
11. Verifikasi Subscription Detail term Archive tidak memuat tombol aksi tulis (Renew, Cancel Subscription)

### TC-AC-CS-592: Read Only dan Group Manager scoped dapat membuka Subscription Log dalam scope READ

12. Klik menu `Client Subscription` di sidebar, klik tab `Current`
13. Logout
14. Login sebagai Read Only `Rina Wijaya`
15. Buka menu Allocation > Client Subscription
16. Ketik Search `SUBS-20260101-00001`, tekan Enter
17. Klik ikon `⋯` pada baris `SUBS-20260101-00001`
18. Verifikasi item `Subscription Log` Show pada row action
19. Klik `Subscription Log`
20. Verifikasi modal Subscription Log terbuka
21. Verifikasi modal tidak memuat aksi tulis
22. Klik `[✕]`
23. Logout
24. Login sebagai Group Manager `Dewi Anggraini`
25. Buka menu Allocation > Client Subscription
26. Klik tab `Current`
27. Ketik Search `SUBS-20250815-00001`, tekan Enter
28. Klik ikon `⋯` pada baris `SUBS-20250815-00001`
29. Verifikasi item `Subscription Log` Show pada baris dalam scope group `Jawa`
30. Klik `Subscription Log`
31. Verifikasi modal Subscription Log terbuka
32. Klik `[✕]`
33. Ganti isi kotak search dengan Subscription ID baris di luar scope READ (`Fixture.license-allocation-subscription.outOfScopeRow`), tekan Enter
34. Verifikasi empty state `No results found` tampil sehingga Subscription Log baris di luar scope tidak dapat dibuka
35. Klik `(←)` pada kotak Search

## Notes

- TC-AC-CS-590 (row action Subscription Log pada semua status) di spec lain suite ini.
- Langkah penghubung (S-03): langkah 7 dan 12 (pindah halaman dan tab), langkah 13 dan 23 (Logout sebagai bagian ganti akun, S-07), langkah 22 dan 32 (menutup modal), langkah 1, 8, 16, 27, dan 33 (Search untuk menemukan baris target, R-16), langkah 15 dan 25 (`Buka menu Allocation > Client Subscription` sesudah login) dan langkah 26 (tab `Current`), dan langkah 35 (mengosongkan Search).
- Ganti akun eksplisit (langkah 13 sampai 14 dan 23 sampai 24) karena akun pertama login di hook `before` (bagian 3a, `[KEPUTUSAN 2026-10-30]`).
- Langkah 34 memakai empty state hasil Search sebagai anchor positif absence baris (bagian 8b butir 2); anchor pemicunya adalah baris dalam scope yang tampil di langkah 28 sampai 29.
- Temuan untuk QA:
  - TC-AC-CS-592 langkah 4 ("Amati baris yang berada di luar scope group Dewi Anggraini") tidak menyebut Subscription ID baris di luar scope; spec memakai baris yang disediakan tim FE.
  - TC-AC-CS-592 Expected a (Read Only) tidak menyebut aksi tulis apa yang diperiksa tidak ada pada modal; spec mengasersi modal tidak memuat tombol aksi tulis sesuai frasa "read-only tanpa aksi tulis".
  - TC-AC-CS-591 Expected b ("sama dengan modal dari row action") tidak punya langkah pembanding terhadap modal row action; spec mengasersi Subscription ID yang sama.
