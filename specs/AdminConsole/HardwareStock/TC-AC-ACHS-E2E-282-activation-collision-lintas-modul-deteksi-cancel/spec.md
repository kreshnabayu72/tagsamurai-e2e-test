---
id: TC-AC-ACHS-E2E-282-activation-collision-lintas-modul-deteksi-cancel
title: "Activation Collision Lintas Modul: Deteksi dan Cancel Request"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-560
  - TC-AC-ACHS-561
  - TC-AC-ACHS-562
coverage:
  web: automated
---

# Activation Collision Lintas Modul: Deteksi dan Cancel Request

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-560 butir c): Client pemohon (akun Client `Fixture.hardwareStock.p23.client[1].name` disediakan tim FE; tidak ada di Pre-setup TC). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals disetel hook `before`/`after` spec ini; seeding Population Stock Pre-setup #16 sampai #23; suite serial `parallel: false` (lihat suite.md).
- Pelaku lintas modul lewat sesi API aktor (kemampuan disediakan tim BE/FE; tidak ada endpoint yang ditulis di spec): Client yang mengaktivasi perangkat di Global Settings > Hardware, Client yang menjalankan Cancel Request, dan Approver Principal lain `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2, `Spectra.env.AC_DEFAULT_USER_PASSWORD`, nama ditetapkan tim FE). Sumber TC modul asal: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (ID 77, 78, 159, 385).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai read-only: SKU `Fixture.hardwareStock.p16.a[2].sku` (Pre-setup #16), Client `Fixture.hardwareStock.p23.client[1].name` dan `Fixture.hardwareStock.p23.client[2].name` (Pre-setup #23).
- Data milik spec (S-06, S-12; target aksi tulis, di-seed hook `before` lewat sesi API aktor dengan struktur yang sama dengan baris Pre-setup yang digantikannya, disediakan tim BE/FE tanpa endpoint karangan; kunci fixture-nya belum ada): unit Active `SN-E2E-{runId}-282A` di Client `Fixture.hardwareStock.p23.client[2].name` sebagai identifier yang sudah Active di Client lain untuk TC-560 (menggantikan unit Pre-setup #18 Tabel F baris ke-5); Subject Activation Collision pending `SN-E2E-{runId}-282B` pada SKU `Fixture.hardwareStock.p16.a[2].sku` (Existing Record Active Client ke-2, requester Client ke-1; TC-561, menggantikan Pre-setup #21 Tabel C baris ke-5); Subject Activation Collision pending `SN-E2E-{runId}-282C` (Existing Record Active Client ke-1, requester Client ke-2; TC-562, menggantikan Pre-setup #21 Tabel C baris ke-11). Data Pre-setup #16 sampai #23 tidak diubah spec ini.
- Cleanup (R-08): hook `after` menghapus secara idempotent unit dan Subject milik spec di atas (`SN-E2E-{runId}-282A` sampai `-282C`) serta Subject Activation Collision baru yang terbentuk dari langkah 4.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuEda` | #16 (Tabel A baris ke-2) | SKU Handheld Reader Range Type Short Range, Total Registered 12 (12 Available, 0 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[2].sku` |
| `snF5` | data milik spec (struktur #18 Tabel F baris ke-5) | Serial Number unit Active milik spec di Client ke-2 | `SN-E2E-{runId}-282A` |
| `snAcEda` | data milik spec (struktur #21 Tabel C baris ke-5) | Matched Identifier Subject Activation Collision pending milik spec pada `skuEda` (Existing Record Active Client ke-2, requester Client ke-1) | `SN-E2E-{runId}-282B` |
| `snAcTc52` | data milik spec (struktur #21 Tabel C baris ke-11) | Matched Identifier Subject Activation Collision pending milik spec (Existing Record Active Client ke-1 Pre-setup #23, requester Client ke-2) | `SN-E2E-{runId}-282C` |
| `client1` | #23 (urutan penulisan daftar Client, butir ke-1) | Nama Client ke-1 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[1].name` |
| `client2` | #23 (urutan penulisan daftar Client, butir ke-2) | Nama Client ke-2 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[2].name` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |

- Waktu: Resolved At TC-561 dibandingkan dengan waktu Cancel Request yang dicatat sesudah aksi dengan toleransi satu menit; jam server dan jam browser sinkron (S-12). Jendela SSE 5 detik adalah pilihan spec (bukan nilai TC atau PRD).
- Baseline: nilai lencana (badge counter) menu Approvals dicatat sebelum aksi (S-12).

## Test Steps

### TC-AC-ACHS-560: Deteksi Activation Collision di Approvals

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Catat nilai lencana (badge counter) menu Approvals
4. Client mengaktivasi perangkat dengan identifier `SN-E2E-{runId}-282A` (sudah Active di `Fixture.hardwareStock.p23.client[2].name`) dari akun Client `Fixture.hardwareStock.p23.client[1].name` lewat sesi API hingga tersimpan; tunggu aksi selesai
5. Muat ulang halaman (F5)
6. Verifikasi Subject `Activation Collision` dengan Matched Identifier `SN-E2E-{runId}-282A` baru tampil di Tab Active dengan Requested By nama Client pemohon `Fixture.hardwareStock.p23.client[1].name`
7. Verifikasi lencana menu Approvals bertambah dari nilai langkah 3

### TC-AC-ACHS-561: Cancel Request oleh Client

8. Buka Hardware > Stock, ketik Search `Fixture.hardwareStock.p16.a[2].sku`, tekan Enter, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[2].sku`
9. Catat jumlah unit pada Summary bar SKU `Fixture.hardwareStock.p16.a[2].sku` (Stock Detail) sebagai nilai awal
10. Buka Approvals > Hardware Stock
11. Klik Tab `Active`
12. Verifikasi Subject `SN-E2E-{runId}-282B` tampil di Tab Active
13. Client menjalankan Cancel Request pada Subject `SN-E2E-{runId}-282B` di Global Settings lewat sesi API hingga pembatalan tersimpan; catat waktu pembatalan; tunggu aksi selesai
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Verifikasi tidak ada toast ke approver
16. Muat ulang halaman (F5)
17. Verifikasi sedikitnya satu Subject lain tampil di Tab Active (pembanding)
18. Verifikasi Subject `SN-E2E-{runId}-282B` hilang dari Tab Active
19. Klik Tab `History`
20. Ketik Search `SN-E2E-{runId}-282B`, tekan Enter
21. Verifikasi Subject tampil di Tab History dengan Approval `Canceled`
22. Verifikasi Approver `—`
23. Verifikasi Resolved At sesuai waktu Cancel Request pada langkah 13 (toleransi satu menit)
24. Klik `(←)` pada kotak Search
25. Buka Hardware > Stock, ketik Search `Fixture.hardwareStock.p16.a[2].sku`, tekan Enter, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[2].sku`
26. Verifikasi unit di Stock Detail tidak berubah: Summary bar sama dengan nilai langkah 9

### TC-AC-ACHS-562: Cancel Request setelah keputusan approver ditolak

27. Buka Approvals > Hardware Stock, lalu klik Tab `Active`
28. Approver Principal (`Fixture.hardwareStock.account.p02.defaultUser.fullName`) menyetujui (Approve) Subject `SN-E2E-{runId}-282C` lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
29. Client menjalankan Cancel Request pada Subject `SN-E2E-{runId}-282C` lewat sesi API
30. Verifikasi Cancel Request ditolak server (respons penolakan; kode status tidak ditetapkan TC)
31. Klik Tab `History`
32. Ketik Search `SN-E2E-{runId}-282C`, tekan Enter
33. Verifikasi Subject tampil dengan Approval `Approved`, bukan `Canceled`
34. Klik `(←)` pada kotak Search
35. Logout, lalu login sebagai Client `Fixture.hardwareStock.p23.client[1].name` (akun Client disediakan tim FE); tunggu aksi selesai

### TC-AC-ACHS-560 (lanjutan): sisi Client

36. Buka Global Settings > Hardware sebagai Client `Fixture.hardwareStock.p23.client[1].name`
37. Verifikasi Client melihat status `Waiting for Approval` pada perangkat `SN-E2E-{runId}-282A`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-560, 561, 562). Tidak ada TC hanya-BE di spec ini.
- Keyword Search pada langkah 20 dan 32 memakai Serial Number penuh Subject milik spec (`SN-E2E-{runId}-282B`, `SN-E2E-{runId}-282C`), bukan potongan; bersuffix `{runId}` sehingga hanya memuat Subject milik spec ini.
- Pembagian TC lintas spec: TC-560 butir c ada di akhir spec ini (langkah 36 dan 37) karena ganti akun ke Client dilakukan paling akhir; butir a dan b TC-560 ada di langkah 6 dan 7.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 8, 10, 11, 19, 25, 27, 31, 36 (navigasi; TC-560 langkah 2 dan TC-561 langkah 2 menulis "Buka Approvals > Hardware Stock Tab Active" dan spec menulis Tab sebagai `Klik Tab` terpisah pada langkah 2, 11, dan 27, `[KEPUTUSAN 2026-11-02]`), 3, 9, 13 (baseline dan mencatat waktu), 4, 13, 28, 29 (pelaku kedua lewat sesi API, R-20), 5, 16 (memuat ulang), 14 (jendela SSE 5 detik sebelum asersi absence, butir 8b), 20 dan 32 (Search untuk menemukan baris target, R-16), 24 dan 34 (mengosongkan Search lewat `(←)`), 35 (ganti akun).
- Langkah 8 dan 25 (Search SKU `Fixture.hardwareStock.p16.a[2].sku` lalu row action `Detail`) adalah langkah penghubung (8b.13, R-16, S-14): langkah 8 membuka Stock Detail sebelum Summary bar dicatat pada langkah 9; Search dibuat di dalam langkah karena Stock List memuat lebih dari satu halaman.
- Anchor positif asersi absence (butir 8b nomor 2): langkah 12 dan 17 (Subject lain tampil) untuk absence Subject di Tab Active (langkah 18); langkah 15 (tidak ada toast) memakai langkah 12 sebagai anchor bahwa halaman Approvals termuat.
- Post Condition TC-560 (notifikasi ke Total Control dan Additional Approver, dicek di TC modul notifikasi) dan TC-561 (identitas Canceled, notifikasi pending diselesaikan) tidak punya langkah observasi di TC dan tidak diasersi; dicatat di Temuan untuk QA.
- Spec ini 37 langkah, lebih dari 35 langkah. Alasan: tiga TC (TC-560 sampai TC-562) satu alur Activation Collision lintas modul dengan satu dataset unit; sesi Client, Approvals, dan Stock Detail harus berurutan dan langkah penghubung navigasi (S-14) tidak bisa dipisah ke spec lain.
- Temuan untuk QA:
  - TC-560 tidak menyebut identifier yang bentrok; spec memakai `SN-E2E-{runId}-282A` (Active di `Fixture.hardwareStock.p23.client[2].name`) dan Client `Fixture.hardwareStock.p23.client[1].name` sebagai pemohon.
  - TC-562 butir a ("Cancel ditolak") tidak menyebut bentuk penolakan (dialog atau status respons); spec mengasersi penolakan server pada level request dan state Tab History (K-1 tidak berlaku karena TC bukan kelas a).
  - Akun Client dan Approver kedua tidak ada di Pre-setup TC; ditulis "disediakan tim FE" (S-11).
  - Seeding unit Active dan Subject milik spec (`SN-E2E-{runId}-282A` sampai `-282C`) beserta cleanup `after` tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE dan kunci fixture-nya belum ada.
