---
id: TC-AC-ACHS-E2E-084-dialog-detail-history-badge-approval-dan-visibilitas-subject
title: "Dialog Detail History, Badge Approval, dan Visibilitas Subject"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-196
  - TC-AC-ACHS-198
  - TC-AC-ACHS-202
  - TC-AC-ACHS-203
coverage:
  web: automated
---

# Dialog Detail History, Badge Approval, dan Visibilitas Subject

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor pertama: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua: Additional Approver dengan capability Create `{Fixture.hardwareStock.account.p06.additionalApproverCreate.email}` (Pre-setup #6, kata sandi `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals diatur hook suite `before` dan dipulihkan `after` (untuk akun Total Control dan untuk akun Additional Approver di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: Approvals Tab History 12 Subject (Pre-setup #22, Tabel D): Approved oleh manusia `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}` (Approver akun Pre-setup #1), Approved oleh `System` `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}`, Rejected `{Fixture.hardwareStock.p22.d[4].matchedIdentifier}`, Canceled `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}`. Seed sesaat Pre-setup #21d: Subject Register Duplicate hasil Sync akun Additional Approver `{Fixture.hardwareStock.p21d.matchedIdentifier}` (SKU `{Fixture.hardwareStock.p16.a[4].sku}`) pending dengan pool Additional Approver yang memiliki anggota lain; dimuat hook `before` spec ini (kemampuan seed disediakan tim BE/FE).

- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p06.additionalApproverCreate.email}` | No 6 | email akun Pre-setup No 6 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}` | No 22, Tabel D baris 1 | Matched Identifier Subject History Canceled, Approver `—` | `Fixture.hardwareStock.p22.d[1].matchedIdentifier` |
  | `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}` | No 22, Tabel D baris 2 | Matched Identifier Subject History Approved oleh user Pre-setup No 1 dengan Approval Note berisi teks | `Fixture.hardwareStock.p22.d[2].matchedIdentifier` |
  | `{Fixture.hardwareStock.p22.d[4].matchedIdentifier}` | No 22, Tabel D baris 4 | Matched Identifier Subject History Rejected (Register Duplicate pada SKU Long Range) | `Fixture.hardwareStock.p22.d[4].matchedIdentifier` |
  | `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}` | No 22, Tabel D baris 7 | Matched Identifier Subject History Approved oleh `System` (Approval Note `—`) | `Fixture.hardwareStock.p22.d[7].matchedIdentifier` |
  | `{Fixture.hardwareStock.p21d.matchedIdentifier}` | No 21d | Matched Identifier Subject Register Duplicate seed sesaat milik akun No 6 pada SKU Long Range (dimuat hook `before`) | `Fixture.hardwareStock.p21d.matchedIdentifier` |

- Unit hasil bypass E2a `SN-ZEBRA-RFD40-{runId}-084` (sumber TC-140, tanpa Subject) disiapkan hook `before` lewat sesi API aktor Total Control (kemampuan fixture disediakan tim BE/FE; unit dibuat dengan Serial Number bersuffix `{runId}` (S-12) yang menggantikan Serial Number literal dari Tabel Data Uji Dinamis TC-140).
- Cleanup (R-08, S-06): hook `after` spec ini menghapus unit bypass `SN-ZEBRA-RFD40-{runId}-084` dan Subject seed sesaat Pre-setup #21d `{Fixture.hardwareStock.p21d.matchedIdentifier}` lewat sesi API aktor Total Control (idempotent: dilewati bila sudah tidak ada; kemampuan disediakan tim BE/FE).

## Test Steps

### TC-AC-ACHS-198: Dialog Detail Tab History, empat varian

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`
3. Klik row action `Detail` pada baris Approved dengan catatan (Matched Identifier `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}`)
4. Verifikasi radio `Approve` pre-selected dan disabled
5. Verifikasi Approval Note berisi teks aktual dan textarea disabled
6. Verifikasi footer `[Close]`
7. Verifikasi judul dialog `Duplicate Identifier Review`
8. Klik `[Close]`
9. Klik row action `Detail` pada baris Approver `System` (Matched Identifier `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}`)
10. Verifikasi Approval Note `—`
11. Verifikasi judul dialog `Duplicate Identifier Review`
12. Klik `[Close]`
13. Klik row action `Detail` pada baris Rejected (Matched Identifier `{Fixture.hardwareStock.p22.d[4].matchedIdentifier}`)
14. Verifikasi radio `Reject` pre-selected dan disabled
15. Verifikasi Approval Note berisi alasan penolakan
16. Verifikasi judul dialog `Duplicate Identifier Review`
17. Klik `[Close]`
18. Klik row action `Detail` pada baris Canceled (Matched Identifier `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}`)
19. Verifikasi radio `Approve` dan `Reject` tidak ditampilkan
20. Verifikasi Approval Note `—`
21. Verifikasi footer `[Close]`
22. Verifikasi judul dialog `Duplicate Identifier Review`
23. Klik `[Close]`

### TC-AC-ACHS-203: Badge kolom Approval Tab History

24. Verifikasi badge `Approved` pada baris Approved berseverity success
25. Verifikasi badge `Rejected` pada baris Rejected berseverity danger
26. Verifikasi badge `Canceled` pada baris Canceled berseverity danger (merah, dibedakan dari Rejected oleh label)

### TC-AC-ACHS-202: Subject requester Total Control (bypass E2a) tidak muncul

27. Klik Tab `Active`
28. Verifikasi sedikitnya satu baris Subject tampil di Tab Active (pembanding)
29. Ketik Search `SN-ZEBRA-RFD40-{runId}-084`, tekan Enter
30. Verifikasi Tab Active menampilkan `No results found`
31. Klik Tab `History`
32. Ketik Search `SN-ZEBRA-RFD40-{runId}-084`, tekan Enter
33. Verifikasi Tab History menampilkan `No results found`
34. Klik `(←)` pada kotak Search

### TC-AC-ACHS-196: Requester Additional Approver tidak melihat Subject permohonannya

35. Klik Tab `Active`
36. Ketik Search `{Fixture.hardwareStock.p21d.matchedIdentifier}`, tekan Enter
37. Verifikasi Subject `{Fixture.hardwareStock.p21d.matchedIdentifier}` tampil di Tab Active akun Total Control (anggota pool lain dapat memutuskan)
38. Klik `(←)` pada kotak Search
39. Logout, lalu login sebagai Additional Approver dengan capability Create (Pre-setup #6); tunggu aksi selesai
40. Buka Approvals > Hardware Stock
41. Pastikan Tab `Active` aktif
42. Verifikasi sedikitnya satu baris Subject tampil di Tab Active (pembanding)
43. Ketik Search `{Fixture.hardwareStock.p21d.matchedIdentifier}`, tekan Enter
44. Verifikasi Subject permohonan sendiri tidak tampil: empty state `No results found`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-196, 198, 202, 203). Tidak ada TC hanya-BE di spec ini.
- Urutan menyimpang dari TC: akun Total Control lebih dulu (TC-198, 203, 202), baru ganti akun ke Additional Approver (TC-196), sesuai bagian 3 (ganti akun eksplisit, bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 8, 12, 17, 23 (navigasi dan menutup dialog), 27, 31, 35, 41 (pindah tab), 34 dan 38 (mengosongkan Search lewat `(←)`, R-16), 39 (ganti akun), 40.
- Langkah 37 adalah asersi tambahan yang tidak ada di TC: Expected TC-196 butir b ("keputusan dilakukan anggota pool lain") tidak punya langkah observasi; spec membuktikannya dengan Subject yang sama terlihat oleh anggota pool lain (akun Total Control). Alasan: mencegah klausa Expected tidak teruji (S-01).
- Langkah 28 dan 42 adalah anchor positif untuk asersi absence (butir 8b nomor 2). Langkah 30 dan 33 memakai empty state `No results found` hasil Search sebagai anchor.
- Spec ini 44 langkah, lebih dari sekitar 35 langkah. Alasan: empat TC satu surface Approvals dengan dataset Subject yang sama; blok sesudah ganti akun (TC-196) tetap bermakna walau blok sebelumnya gagal, dan tiap blok berdiri sendiri.
- Temuan untuk QA:
  - Tabel Data Uji Pre-setup #22 tidak menyebut baris Approved mana yang memuat catatan; spec memakai `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}` sebagai baris Approved dengan catatan dan `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}` (Approver `System`) untuk Approval Note `—`.
  - TC-198 butir b menyebut "Approved tanpa catatan" selain Approver `System` tetapi langkah TC hanya membuka baris `System`; satu `Verifikasi` Approval Note `—` dipakai untuk keduanya.
  - TC-202 bergantung pada keberadaan unit bypass hasil TC-140; spec menyiapkannya lewat fixture BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD).
  - TC-196 menyebut pool memiliki anggota lain tanpa menyebut siapa; Total Control diasumsikan anggota pool (Pre-setup #1 memuat "anggota approver pool").
