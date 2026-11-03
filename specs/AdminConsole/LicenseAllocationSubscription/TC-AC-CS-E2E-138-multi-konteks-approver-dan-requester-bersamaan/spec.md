---
id: TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan
title: "Multi-konteks: Approver dan Requester Bersamaan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-518
  - TC-AC-CS-519
  - TC-AC-CS-520
  - TC-AC-CS-578
coverage:
  web: automated
---

# Multi-konteks: Approver dan Requester Bersamaan

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks). Akun aktor pertama (sesi A): Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, approver), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Akun ganti akun dan sesi B (Test Steps memuat langkah Logout, login, dan pembukaan konteks kedua eksplisit):

| Pre-setup | Email | Peran | Dipakai di | Env password |
|---|---|---|---|---|
| #6 | `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`) | Create-Only Distributor, requester | sesi B TC-AC-CS-519 (UI), sesi UI TC-AC-CS-520, sesi API pemicu TC-AC-CS-518 dan 578 | `Spectra.env.AC_SUB_CREATE_PASSWORD` |
| #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager Distributor, bypass | sesi UI TC-AC-CS-578 | `Spectra.env.AC_SUB_GM_PASSWORD` |
| #9 | akun sesi A di atas (`Eko Saputra`) | Total Control Distributor | sesi API pemicu Approve TC-AC-CS-578 | `Spectra.env.AC_SUB_DIST_TC_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- State global: toggle Require Approval for Allocation PT Maju Bersama diatur ON oleh fixture backend yang disediakan tim FE/BE di hook `before` dan dipulihkan ke nilai awal di hook `after` (S-06, pengecualian 2026-10-30); saldo Main Pocket $25,000.00 (Pre-setup #20) dan harga SAMS Professional $7,000.00 untuk TC-AC-CS-578 diatur lewat fixture. Suite berjalan serial.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-138`): pengajuan Waiting for Approval `W518`, `W519`, dan `W520` (Subscription ID tiap pengajuan dibaca lewat API seeding dan dipakai sebagai `W518`, `W519`, `W520` pada Test Steps) milik requester `Fajar Nugroho` pada Client seed `Klinik Pengajuan+{runId}-138` (setara Pre-setup #49); trial pada Client `Klinik Harapan Bunda+{runId}-138` (Subscription ID-nya dibaca lewat API seeding dan dipakai sebagai `T578`) SAMS Growth Active (Plan Owner CV Karya Mandiri, tanpa term paid SAMS; setara Pre-setup #71).
- Kemampuan teknis (disediakan tim FE/BE): konteks browser kedua yang menekan tombol bersamaan dengan sesi A (sinkronisasi klik oleh runner); sesi API aktor requester dan approver (token API tidak dihitung sebagai sesi web); membaca jumlah Reserve/Capture Wallet; endpoint tulis tidak tertulis di TC, PRD, atau LLD (S-13). Konteks sesi B ditutup dan sesi login browser terkait dihapus di akhir TC-AC-CS-519 (S-09).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen` untuk akun UI suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-518: Approve ditolak bila requester menyimpan Edit setelah approver membuka Review

1. Buka Approvals > Client Subscription
2. Ketik Search `W518`, tekan Enter
3. Buka Review pengajuan `W518`
4. Picu lewat sesi API aktor `Fajar Nugroho`: Save Edit Duration `W518` hingga perubahan tersimpan
5. Pilih radio Approve, klik `[Submit Decision]`
6. Verifikasi dialog blok milik Approvals dengan Title "Transaction Data Has Changed" dan tombol tunggal `[OK]`
7. Klik `[OK]`
8. Verifikasi keputusan tidak diproses dan nilai pada Review di-reset ke data terbaru
9. Verifikasi status `W518` tetap Waiting for Approval

### TC-AC-CS-519: Approve bersamaan Cancel Request: first-write-wins

10. Ganti isi kotak search dengan `W519`, tekan Enter
11. Buka Review pengajuan `W519` dan pilih radio Approve (sesi A)
12. Buka sesi B (konteks browser kedua), login sebagai Create-Only `Fajar Nugroho`, buka Allocation > Client Subscription tab Current
13. Pada sesi B ketik Search `W519`, tekan Enter
14. Pada sesi B klik ikon `⋯` pada `W519`, klik `Cancel Request` (dialog terbuka)
15. Sesi B klik `[Cancel Request]` dan sesi A klik `[Submit Decision]` hampir bersamaan
16. Tunggu aksi selesai (respons kedua sesi diproses)
17. Baca status akhir `W519` lewat fixture backend (disediakan tim FE/BE; hasil race tidak menentukan tab yang menampilkan baris)
18. Verifikasi hanya satu keputusan yang berlaku (yang lebih dulu commit): status akhir `W519` Approved atau Canceled
19. Verifikasi pihak yang kalah menerima penolakan; bila Cancel Request yang kalah, sesi B menampilkan dialog "Cannot Cancel Request" dengan teks "This request has already been approved."
20. Verifikasi tidak ada Reserve atau Capture ganda pada Wallet
21. Tutup dialog atau form yang tersisa pada sesi A dan sesi B dengan klik menu `Client Subscription` di sidebar
22. Tutup konteks sesi B dan hapus sesi login browser terkait

### TC-AC-CS-520: Edit bersamaan Cancel Request pada pengajuan yang sama

23. Logout
24. Login sebagai Create-Only `Fajar Nugroho`
25. Buka menu `Allocation > Client Subscription`
26. Ketik Search `W520`, tekan Enter
27. Klik ikon `⋯` pada `W520`, klik `Edit`, ubah Duration
28. Picu lewat sesi API aktor `Fajar Nugroho`: Cancel Request `W520` hingga pengajuan Canceled tersimpan
29. Klik `[Save]` pada form Edit
30. Verifikasi dialog blok Title "Cannot Update Subscription" dengan teks "This request can no longer be edited."
31. Verifikasi data `W520` tidak berubah
32. Klik `✕` pada form Edit
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

### TC-AC-CS-578: Convert ditolak bila trial sudah Converted lewat Approve jalur request

35. Logout
36. Login sebagai Group Manager `Dewi Anggraini`
37. Buka menu `Allocation > Client Subscription`
38. Ketik Search `T578`, tekan Enter
39. Klik ikon `⋯` pada trial `T578`, klik `Convert Trial` (modal terbuka)
40. Picu lewat sesi API aktor: `Fajar Nugroho` (toggle ON) mengajukan Convert pada trial `T578`, lalu `Eko Saputra` meng-Approve pengajuan itu hingga trial Converted dan term paid Active tersimpan
41. Pilih Plan `Professional`, isi Duration `1`, klik `[Submit]`, klik `[Convert]`
42. Verifikasi dialog blok Title "Data has changed"
43. Verifikasi Body dialog "• Klinik Harapan Bunda+{runId}-138 — SAMS" dan "This trial has already been converted by another user."
44. Verifikasi dialog hanya memuat tombol tunggal `[OK]`
45. Klik `[OK]`
46. Verifikasi daftar memuat ulang
47. Klik tab `History`
48. Ganti isi kotak search dengan `T578`, tekan Enter
49. Verifikasi baris trial `T578` tampil berstatus Converted
50. Verifikasi tidak ada term paid kedua, tidak ada Reserve atau Capture dari sesi Group Manager, dan tidak ada record Convert kedua

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Kelas c: pada TC-AC-CS-519 sesi UI kedua adalah objek asersi (dialog "Cannot Cancel Request" tampil di sesi B), sehingga `P-2` tidak dipakai; pada TC-AC-CS-518, 520, 578 pelaku kedua memakai sesi API (bukan konteks kedua) dan hanya memicu perubahan state.
- Langkah penghubung (S-03): langkah 2, 10, 13, 26, dan 38 (Search untuk menemukan baris target sebelum aksi baris, R-16), langkah 21 (menutup dialog atau form tersisa), langkah 16 (menunggu respons kedua sesi diproses sebelum membaca status lewat fixture, 8b.8), langkah 25 dan 37 (membuka List sesudah login ganti akun, S-07), langkah 22 (menutup konteks kedua, S-09), langkah 32 sampai 34 (menutup form dirty, S-08), langkah 47 dan 48 (pindah tab History dan Search untuk menemukan baris target, R-16), serta langkah 23 sampai 24 dan 35 sampai 36 (Logout dan login sebagai ganti akun, S-07).
- Spec ini melewati ~35 langkah (50). Alasan: semua blok satu kelas harness (multi-konteks approver dan requester) dan berdiri sendiri dengan pengajuan milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan akun-akun hanya dipakai satu kali berurutan.
- Temuan untuk QA:
  - TC-AC-CS-518, 519, 520, 578 ditandai `Manual Only — (d) dua sesi paralel` di kolom Automation; spec mengotomasikannya dengan pemicu sesi API dan sinkronisasi klik oleh runner (kemampuan disediakan tim FE/BE).
  - TC-AC-CS-519 Expected b/c: hasil race tidak dapat dipaksa; langkah 17 sampai 18 dan 19 mengasersi hasil pemenang mana pun dan dialog hanya bila Cancel Request yang kalah.
  - TC-AC-CS-518 langkah 1 tidak menyebut kontrol Approve dan dialog konfirmasi; spec memakai radio Approve dan `[Submit Decision]` seperti pola Approvals di tempat lain (TC-AC-CS-477) tanpa dialog konfirmasi.
  - TC-AC-CS-520 langkah 1 menyebut klik `[Save]` tanpa menyebut field yang diubah; spec mengubah Duration.
  - TC-AC-CS-578 menyebut Post Condition (term paid Active di tab `Current`, trial Converted di `History`) tanpa langkah observasi tambahan; Post Condition a tidak diasersi (S-01), Post Condition b diasersi lewat Expected b (langkah 49).
