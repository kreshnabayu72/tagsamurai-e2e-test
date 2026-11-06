---
id: TC-FA-TAG-E2E-389-absence-log-request-langsung-receive-dan-decline-report-ditolak-tidak-menulis-event-log-tag-log-changelog
title: "Absence Log: Request Langsung Receive TAG, Receive Manually, dan Decline Report yang Ditolak 403 Tidak Menulis Event Log, TAG Log, dan Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1290
  - TC-FA-TAG-1291
  - TC-FA-TAG-1292
  - TC-FA-TAG-1293
  - TC-FA-TAG-1294
coverage:
  web: automated
---

# Absence Log: Request Langsung Receive TAG, Receive Manually, dan Decline Report yang Ditolak 403 Tidak Menulis Event Log, TAG Log, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 2 | Manage asset & TAG dengan Update di group Disposal Center | `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_PASSWORD` |
| 3 | Manage asset & TAG (Read) | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Read Only (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 3; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) kemampuan baca jumlah entri Event Log dan TAG Log per Tag serta Changelog Paired TAG sebelum dan sesudah request (baseline per TC, S-12, butir A-18); (3) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dan laporan terbuka. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (pengecualian S-06/S-12 butir A-15; kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE; tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.) dipakai sebagai precondition TC, tidak diasersi; [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |
| Reason | Tag masih terbaca | `reasonDecline` |

- State yang diubah dan pemulihannya: tidak ada (semua request ditolak); hook `after` memastikan Tag To Be Returned dan laporan RF-00130 dalam keadaan awal dan sesi ke akun default suite. Efek yang tidak terpulihkan: tidak ada entri baru yang dibuat spec ini; Event Log, TAG Log, dan Changelog adalah audit trail permanen dan tidak dipulihkan fixture (butir A-18).

## Test Steps

### TC-FA-TAG-1290: Read Only, commit Receive TAG langsung untuk RF-00071

1. Catat baseline jumlah entri Event Log dan TAG Log Tag RF-00071 lewat kemampuan baca (N1 untuk Event Log, N2 untuk TAG Log)
2. Kirim request commit Receive TAG untuk RF-00071 langsung ke server lewat klien HTTP memakai token pengguna Read Only
3. Verifikasi server membalas 403
4. Verifikasi jumlah entri Event Log Tag RF-00071 tidak bertambah dibanding N1
5. Verifikasi jumlah entri TAG Log Tag RF-00071 tidak bertambah dibanding N2

### TC-FA-TAG-1294: Read Only, commit Decline Report langsung untuk RF-00130

6. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N3)
7. Kirim request commit Decline Report untuk RF-00130 dengan Reason "Tag masih terbaca" langsung ke server lewat klien HTTP memakai token pengguna Read Only
8. Verifikasi server membalas 403
9. Verifikasi jumlah entri Changelog Paired TAG tidak bertambah dibanding N3

### Ganti akun

10. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG dengan Update di group Disposal Center

### TC-FA-TAG-1291: Update di group Disposal Center, commit Receive TAG langsung untuk NF-00092

11. Catat baseline jumlah entri Event Log dan TAG Log Tag NF-00092 lewat kemampuan baca (N4 untuk Event Log, N5 untuk TAG Log)
12. Kirim request commit Receive TAG untuk NF-00092 (Return Group HQ Warehouse) langsung ke server lewat klien HTTP memakai token pengguna
13. Verifikasi server membalas 403
14. Verifikasi jumlah entri Event Log Tag NF-00092 tidak bertambah dibanding N4
15. Verifikasi jumlah entri TAG Log Tag NF-00092 tidak bertambah dibanding N5

### TC-FA-TAG-1293: Update di group Disposal Center, commit Receive Manually langsung untuk NF-00092

16. Catat baseline jumlah entri Event Log dan TAG Log Tag NF-00092 lewat kemampuan baca (N6 untuk Event Log, N7 untuk TAG Log)
17. Kirim request commit Receive Manually untuk NF-00092 (HQ Warehouse) dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP
18. Verifikasi server membalas 403
19. Verifikasi jumlah entri Event Log Tag NF-00092 tidak bertambah dibanding N6
20. Verifikasi jumlah entri TAG Log Tag NF-00092 tidak bertambah dibanding N7

### Ganti akun

21. Logout dari akun Manage asset & TAG dengan Update di group Disposal Center, lalu Login sebagai akun Manage asset & TAG (Read)

### TC-FA-TAG-1292: Manage asset & TAG (Read), commit Receive Manually langsung untuk RF-00071

22. Catat baseline jumlah entri Event Log dan TAG Log Tag RF-00071 lewat kemampuan baca (N8 untuk Event Log, N9 untuk TAG Log)
23. Kirim request commit Receive Manually untuk RF-00071 dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP memakai token pengguna
24. Verifikasi server membalas 403
25. Verifikasi jumlah entri Event Log Tag RF-00071 tidak bertambah dibanding N8
26. Verifikasi jumlah entri TAG Log Tag RF-00071 tidak bertambah dibanding N9

## Notes

- Spec absence (kelas g, S-05). Pemicu (request langsung ke server yang ditolak 403, kelas a) bukan objek uji; `P-5` butir (a). Tiap TC punya user dan baseline sendiri (langkah 1, 6, 11, 16, 22); baseline dibaca ulang sebelum tiap pemicu karena Tag yang sama dipakai TC lain di spec ini (NF-00092 pada TC-FA-TAG-1291 dan TC-FA-TAG-1293; butir A-18).
- Pembagian TC lintas spec (S-05): TC-FA-TAG-1290, TC-FA-TAG-1291, TC-FA-TAG-1292, TC-FA-TAG-1293, dan TC-FA-TAG-1294 ada juga di spec 329, tempat respons 403 serta status Tag atau laporan diasersi. Spec ini hanya memuat klausa "tidak ada entri Event Log, TAG Log, atau Changelog baru" dengan request langsung sebagai pemicu.
- Urutan blok mengikuti akun aktor (satu ganti akun per blok), bukan urutan nomor TC: TC-FA-TAG-1290 dan 1294, lalu 1291 dan 1293, lalu 1292.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 dan 21 (ganti akun). Langkah Catat baseline (1, 6, 11, 16, 22) adalah aksi baca (S-12).
- Anchor positif absence (bagian 8b butir 2): langkah 3, 8, 13, 18, dan 24 (`Verifikasi` respons 403 atas pemicu yang sama, butir Expected TC) mendahului tiap asersi jumlah entri; jumlah awal yang dicatat adalah pembanding pada surface yang sama. Surface Event Log dan TAG Log diasersi satu per satu (langkah 4 dan 5, 14 dan 15, 19 dan 20, 25 dan 26).
- Total entri Event Log, TAG Log, dan Changelog tidak diasersi sebagai angka absolut (S-12); semua asersi jumlah memakai selisih terhadap baseline N1 sampai N9.
- Butir A-15: nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; seeding idempotent dan pemulihan lewat fixture backend (suite serial).
- Temuan untuk QA:
  - TC-FA-TAG-1293 Expected butir b ("tidak ada entri baru") tidak menyebut surface; spec memakai Event Log dan TAG Log seperti TC-FA-TAG-1291.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
