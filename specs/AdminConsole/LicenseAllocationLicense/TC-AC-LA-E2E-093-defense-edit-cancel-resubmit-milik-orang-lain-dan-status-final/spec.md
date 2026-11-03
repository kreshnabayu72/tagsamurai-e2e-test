---
id: TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final
title: "Defense-in-Depth: Edit, Cancel, dan Resubmit Milik Orang Lain dan pada Status Final"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-82
  - TC-AC-LA-222
  - TC-AC-LA-199
  - TC-AC-LA-233
  - TC-AC-LA-200
  - TC-AC-LA-223
  - TC-AC-LA-234
coverage:
  web: automated
---

# Defense-in-Depth: Edit, Cancel, dan Resubmit Milik Orang Lain dan pada Status Final

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager approve-only `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`, Pre-setup #8), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19), Bengkel Cahaya Motor (#23), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Waiting for Approval` Concurrent User +5 milik `Dewi A` (bentuk #41) untuk TC-AC-LA-222 dan TC-AC-LA-199; alokasi `Canceled` manual milik `Dewi A` (bentuk #48) untuk TC-AC-LA-233; satu seed per status final milik `Dewi A` untuk TC-AC-LA-200, 223, 234: `Active` (bentuk #47), `Rejected` (bentuk #50), `Canceled` manual (bentuk #48), `Expired` (bentuk #76). Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit, Edit, Cancel, dan Resubmit langsung ke server memakai sesi API akun aktor masing-masing (login API tidak dihitung sebagai sesi web, `suite.md`), membaca status dan jumlah record lewat fixture BE (tanpa mengarang endpoint, S-13).
- Tabel parameter blok status final (dipakai langkah 24 sampai 28):

| Status seed | TC-AC-LA-200 (Edit) | TC-AC-LA-223 (Cancel) | TC-AC-LA-234 (Resubmit) |
|---|---|---|---|
| `Active` | ya | ya | ya |
| `Rejected` | ya | ya | ya |
| `Canceled` | ya | tidak | tidak |
| `Expired` | ya | ya | ya |

- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-82: Group Manager approve-only tidak dapat Allocate, Edit, atau Resubmit

1. Catat jumlah alokasi PT Sejahtera lewat fixture BE sebagai baseline, lalu periksa toolbar tab Current
2. Verifikasi `[+ Allocation]` Hidden (anchor: Table Tools tampil di toolbar yang sama)
3. Buka menu `⋯` pada baris `Waiting for Approval` dan baris Canceled di tab History
4. Verifikasi row action `Edit` Hidden
5. Verifikasi row action `Resubmit` Hidden
6. Kirim request submit alokasi langsung ke server dengan akun ini
7. Verifikasi respons server menolak dengan penolakan akses
8. Verifikasi tidak ada record baru (jumlah alokasi PT Sejahtera sama dengan baseline langkah 1)

### TC-AC-LA-222: Cancel oleh Group Manager pada Waiting for Approval milik orang lain

9. Buka menu `⋯` pada baris `Waiting for Approval` milik `Dewi A`
10. Verifikasi `Cancel Allocation` tidak tersedia
11. Kirim request Cancel langsung untuk record itu
12. Verifikasi respons server menolak
13. Verifikasi status record tidak berubah

### TC-AC-LA-199: Edit oleh selain requester original ditolak

14. Ganti akun: logout `Rian H`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
15. Kirim request Edit langsung untuk record `Waiting for Approval` milik `Dewi A`
16. Verifikasi respons server menolak (aktor bukan requester original)
17. Verifikasi record tidak berubah

### TC-AC-LA-233: Resubmit oleh selain requester original ditolak

18. Klik tab `History` dan buka menu `⋯` pada baris Canceled milik `Dewi A`
19. Verifikasi `Resubmit` tidak tersedia
20. Kirim request Resubmit langsung untuk record itu
21. Verifikasi respons server menolak
22. Verifikasi tidak ada record baru

### TC-AC-LA-200, TC-AC-LA-223, dan TC-AC-LA-234: Aksi pada record status final ditolak

23. Ganti akun: logout `Fajar N`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`

Untuk setiap aksi (Edit, Cancel, Resubmit) dan setiap status seed yang bertanda "ya" pada tabel parameter (langkah 24 sampai 28):

24. Kirim request aksi langsung untuk record seed berstatus tersebut milik sendiri
25. Verifikasi respons server menolak (Edit dan Cancel: respons error generik; Resubmit: ditolak)
26. Verifikasi record tidak berubah (Edit dan Cancel) atau tidak ada record baru (Resubmit)
27. Buka menu `⋯` baris seed berstatus tersebut
28. Verifikasi row action aksi itu (`Edit`, `Cancel Allocation`, atau `Resubmit`) tidak tersedia

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar semua TC satu akun berurutan sebelum ganti akun.
- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend. TC-AC-LA-82, 222, 233, 200, 223, 234 juga memuat bagian UI (visibilitas row action) yang diasersi di browser.
- Langkah 24 sampai 28 diulang untuk 4 status pada TC-AC-LA-200, 3 status pada TC-AC-LA-223, dan 3 status pada TC-AC-LA-234 (10 iterasi, 8b butir 7), parameter pada tabel Prerequisites. Setiap Verifikasi tetap satu per klausa.
- Langkah penghubung (S-03): langkah 3, 9, 18, 27 (membuka menu `⋯`), 14 dan 23 (ganti akun). Langkah 1 mencatat baseline (S-12).
- Asersi `Hidden` atau tidak tersedia (langkah 2, 4, 5, 10, 19, 28) beranchor Table Tools dan menu `⋯` yang tampil (8b butir 2).
- Spec melewati sekitar 35 langkah setelah ekspansi iterasi. Alasan pertahanan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) pada topik yang sama (aksi tulis oleh bukan pemilik atau pada status final) dan tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-LA-82, 222, 199, 233, 200, 223, 234 menyebut "respons error generik" atau "penolakan akses" tanpa status HTTP; spec mengasersi penolakan tanpa kode.
  - TC-AC-LA-82 Langkah 1 ("Periksa toolbar") tidak menyebut baris tempat row action `Edit` dan `Resubmit` diperiksa; spec memakai baris `Waiting for Approval` dan Canceled.
  - TC-AC-LA-200 Precondition menyebut alokasi Expired milik `Dewi A` (Pre-setup #76) pada tab Current, padahal Expired berada di tab History; spec membuka baris di tab yang sesuai statusnya.
  - TC-AC-LA-223 dan TC-AC-LA-234 tidak menyebut status `Canceled` (TC-AC-LA-223: selain Canceled; TC-AC-LA-234: selain Canceled); tabel parameter mengikutinya.
