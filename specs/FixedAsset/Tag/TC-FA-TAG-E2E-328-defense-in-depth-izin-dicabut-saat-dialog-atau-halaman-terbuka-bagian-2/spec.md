---
id: TC-FA-TAG-E2E-328-defense-in-depth-izin-dicabut-saat-dialog-atau-halaman-terbuka-bagian-2
title: "Defense-in-Depth: Hak Update Dicabut saat Dialog Receive TAG, Receive Manually, atau Decline Report Terbuka, Commit Ditolak Server (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1303
  - TC-FA-TAG-1304
  - TC-FA-TAG-1305
coverage:
  web: automated
---

# Defense-in-Depth: Hak Update Dicabut saat Dialog Receive TAG, Receive Manually, atau Decline Report Terbuka, Commit Ditolak Server (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Manage asset & TAG dengan Update di group Disposal Center | `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_PASSWORD` |
| 2 | Manage asset & TAG dengan Update di group Plant B | `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PB_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: blok 1. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 2; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag; (2) pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`) yang mencabut dan memulihkan Update pengguna pada group di Settings > Role & Permission, tanpa asersi di sesinya; akun Admin disediakan tim FE; (3) pembacaan state data lewat fixture backend (status Tag, status laporan, jumlah entri Event Log dan TAG Log; baseline dicatat di hook `before`); (4) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dan laporan terbuka; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |

- State yang diubah dan pemulihannya: Update pengguna blok 1 pada group Disposal Center dicabut di langkah 4 dan 14 serta dipulihkan di langkah 9 dan 19; Update pengguna blok 2 pada group Plant B dicabut di langkah 27 dan dipulihkan di langkah 31. Hook `after` memulihkan capability pengguna dan sesi walau spec gagal di tengah.

## Test Steps

### Blok 1: Update di group Disposal Center (TC-FA-TAG-1303, TC-FA-TAG-1304)

1. Klik tab `To Be Returned`
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00071
4. Pelaku kedua (Admin) mencabut Update pengguna pada group Disposal Center lewat sesi API hingga tersimpan
5. Klik tombol [Receive]
6. Verifikasi server menolak commit dengan 403
7. Verifikasi Tag RF-00071 tetap To Be Returned
8. Verifikasi jumlah entri Event Log dan TAG Log RF-00071 tidak bertambah dibanding baseline
9. Pelaku kedua memulihkan Update pengguna pada group Disposal Center lewat sesi API hingga tersimpan
10. Muat ulang halaman (F5)
11. Klik tab `To Be Returned`
12. Buka menu aksi baris RF-00071
13. Klik "Receive Manually"
14. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
15. Pelaku kedua (Admin) mencabut Update pengguna pada group Disposal Center lewat sesi API hingga tersimpan
16. Klik tombol [Submit]
17. Verifikasi server menolak commit dengan 403
18. Verifikasi Tag RF-00071 tetap To Be Returned
19. Pelaku kedua memulihkan Update pengguna pada group Disposal Center lewat sesi API hingga tersimpan
20. Muat ulang halaman (F5)

### Blok 2: Update di group Plant B (TC-FA-TAG-1305)

21. Logout dari akun Update di group Disposal Center, lalu Login sebagai akun Manage asset & TAG dengan Update di group Plant B
22. Buka Fixed Asset > TAG > Paired
23. Klik Asset Name 'Excavator 20 Ton' pada baris group Plant B untuk membuka Popup Detail
24. Buka menu aksi baris 'Excavator 20 Ton - 20'
25. Klik "Decline Report"
26. Isi Textarea "Reason" dengan "Tag masih terbaca"
27. Pelaku kedua (Admin) mencabut Update pengguna pada group Plant B lewat sesi API hingga tersimpan
28. Klik tombol [Submit]
29. Verifikasi server menolak commit dengan 403
30. Verifikasi laporan RF-00130 tetap terbuka
31. Pelaku kedua memulihkan Update pengguna pada group Plant B lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1303 s.d. 1305). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1281 s.d. 1283 ada di spec 327 dan TC-FA-TAG-1284 serta TC-FA-TAG-1313 ada di spec 352.
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 4, 9, 15, 19, 27, 31).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 19, dan 31 (memulihkan capability), 10 dan 20 (muat ulang halaman untuk menutup dialog dirty dan menyegarkan capability di UI; dialog `beforeunload` ditangani sesuai Prerequisites), 21 (ganti akun), 22 (membuka halaman sesudah login akun lain).
- Asersi "jumlah entri Event Log dan TAG Log tidak bertambah" (langkah 8) ditulis di spec ini dengan baseline (S-12) dan didahului `Verifikasi` respons penolakan dan status Tag sebagai anchor; spec absence kelas g milik modul ini tidak memuat TC-FA-TAG-1303.
- Temuan untuk QA:
  - TC-FA-TAG-1303 s.d. 1305 menyebut "Pengguna A" dan "Admin" tanpa akun; spec memakai akun Pre-setup sebagai Pengguna A dan Admin lewat sesi API yang disediakan tim FE.
  - TC-FA-TAG-1304 dan TC-FA-TAG-1305 tidak memberi langkah observasi untuk entri Event Log atau TAG Log; spec hanya mengasersi Expected TC (penolakan 403 dan status Tag atau laporan).
  - TC-FA-TAG-1305 tidak menyebut langkah membuka Popup Detail dan menu aksi; spec memakai urutan yang sama dengan TC Decline Report lain (Popup Assets group Plant B, menu aksi baris, "Decline Report").
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
