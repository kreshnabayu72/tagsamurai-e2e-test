---
id: TC-AC-CS-E2E-025-scope-tulis-group-manager-descendant-dan-opsi-new-client
title: "Scope Tulis: Group Manager Descendant dan Opsi New Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-98
  - TC-AC-CS-99
coverage:
  web: automated
---

# Scope Tulis: Group Manager Descendant dan Opsi New Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager scope Group `Jawa` beserta descendant, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain untuk TC-AC-CS-99 (ganti akun eksplisit di langkah): Create-Only Distributor tanpa Manage active client (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), `Spectra.env.AC_SUB_CREATE_PASSWORD`; Create pada Manage allocation dan Manage active client (Pre-setup #92) `createClientSub_automated_{namaCompany}@qwertysystem.net` (`Bayu Setiawan`), `Spectra.env.AC_SUB_CREATECLIENT_PASSWORD`; Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): empat Client binaan langsung PT Maju Bersama, masing-masing dengan satu term Active, bernama `GMScope+{runId}-025 Jawa` (group `Jawa`), `GMScope+{runId}-025 Jawa Barat` (group `Jawa Barat`, child `Jawa`), `GMScope+{runId}-025 Bandung` (group `Bandung`, cucu `Jawa`), dan `GMScope+{runId}-025 Sumatera` (group `Sumatera`, di luar scope Group Manager). Padanan struktur group Pre-setup #5 dan #89.
- Tidak ada aksi tulis dan tidak ada perubahan state global; form `+ Subscription` hanya dibuka lalu ditutup tanpa Submit.

## Test Steps

### TC-AC-CS-98: Group Manager mencakup descendant dari group yang di-assign

1. Ketik Search `GMScope+{runId}-025 Bandung`, tekan Enter
2. Verifikasi baris Client `GMScope+{runId}-025 Bandung` tampil di tab Current
3. Ganti isi kotak search dengan `GMScope+{runId}-025 Jawa Barat`, tekan Enter
4. Verifikasi baris Client `GMScope+{runId}-025 Jawa Barat` tampil
5. Ganti isi kotak search dengan `GMScope+{runId}-025 Jawa`, tekan Enter
6. Verifikasi baris Client `GMScope+{runId}-025 Jawa` tampil
7. Ganti isi kotak search dengan `GMScope+{runId}-025`, tekan Enter
8. Verifikasi tepat tiga baris tampil, yaitu Client `Jawa`, `Jawa Barat`, dan `Bandung`
9. Verifikasi baris Client `GMScope+{runId}-025 Sumatera` tidak tampil
10. Ganti isi kotak search dengan `GMScope+{runId}-025 Sumatera`, tekan Enter
11. Verifikasi tidak ada baris Client `GMScope+{runId}-025 Sumatera` pada hasil Search
12. Klik `(←)` pada kotak Search

### TC-AC-CS-99: Opsi `[+ New Client]` hanya untuk aktor dengan Manage active client Create

13. Logout, lalu login sebagai Create-Only Distributor `Fajar Nugroho` (Pre-setup #6)
14. Buka menu Allocation > Client Subscription
15. Klik `[+ Subscription]`, lalu buka dropdown Client
16. Verifikasi opsi Client `GMScope+{runId}-025 Jawa` tampil di dropdown Client
17. Verifikasi opsi `[+ New Client]` tidak tampil di dropdown Client untuk Create-Only tanpa Manage active client
18. Tekan `Esc` untuk menutup dropdown, lalu klik `[✕]` pada header modal
19. Logout, lalu login sebagai Create-Only Distributor `Bayu Setiawan` (Pre-setup #92)
20. Buka menu Allocation > Client Subscription
21. Klik `[+ Subscription]`, lalu buka dropdown Client
22. Verifikasi opsi `[+ New Client]` tampil di dropdown Client untuk `Bayu Setiawan`
23. Tekan `Esc` untuk menutup dropdown, lalu klik `[✕]` pada header modal
24. Logout, lalu login sebagai Total Control Distributor `Eko Saputra` (Pre-setup #9)
25. Buka menu Allocation > Client Subscription
26. Klik `[+ Subscription]`, lalu buka dropdown Client
27. Verifikasi opsi `[+ New Client]` tampil di dropdown Client untuk Total Control Distributor
28. Tekan `Esc` untuk menutup dropdown, lalu klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16) pada langkah 1, 3, 5, 7, 10; `(←)` pada kotak Search (langkah 12); `Buka menu Allocation > Client Subscription` sesudah tiap ganti akun (langkah 14, 20, 25; S-07/8b.6); `Esc` dan `[✕]` menutup dropdown dan modal bersih (langkah 18, 23, 28; form tidak dirty sehingga tidak ada dialog Unsaved Changes, S-08 tidak berlaku).
- Anchor absence (butir 8b.2): langkah 8 (tiga baris tampil) mendahului langkah 9, langkah 16 (opsi Client lain tampil) mendahului langkah 17.
- Ganti akun eksplisit di langkah 13, 19, 24 (S-07); akun pertama login di hook `before`.
- TC-AC-CS-98 Langkah 1 dan 2 menyebut Search untuk Client di group `Bandung` dan `Sumatera` tanpa menamai Client dan tanpa menyatakan apakah Client punya term; spec memakai seed sendiri di Prerequisites. Ekspektasi a menyebut tiga group sedangkan langkah hanya mencari dua; spec mencari ketiganya (langkah 1 sampai 6).
- Temuan untuk QA:
  - TC-AC-CS-98: nama Client di group `Jawa`, `Jawa Barat`, `Bandung`, dan `Sumatera` tidak ada di Data Uji Pre-setup (hanya #89 `Toko Bandung Raya` untuk group `Bandung`); spec memakai seed bersuffix.
  - TC-AC-CS-99: judul TC dan Langkah 2 menyebut login "Create-Only" untuk akun `Bayu Setiawan` (#92) yang juga punya Create pada Manage active client; spec mengikuti Expected b.
  - Kolom ACC indeks perencanaan menyebut aktor Group Manager dan Create-Only; akun #92 dan #9 hanya muncul di Precondition TC-AC-CS-99 dan dituliskan di Prerequisites.
