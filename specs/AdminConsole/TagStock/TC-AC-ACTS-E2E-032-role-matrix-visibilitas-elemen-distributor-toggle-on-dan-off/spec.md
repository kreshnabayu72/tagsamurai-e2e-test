---
id: TC-AC-ACTS-E2E-032-role-matrix-visibilitas-elemen-distributor-toggle-on-dan-off
title: "Role Matrix: Visibilitas Elemen TAG > Stock oleh Distributor dengan Toggle Local Registration ON dan OFF"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-122
  - TC-AC-ACTS-123
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen TAG > Stock oleh Distributor dengan Toggle Local Registration ON dan OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Distributor Toggle ON`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Distributor Toggle ON (#9) | `distributorOn_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_ON_PASSWORD` |
| 2 | Distributor Toggle OFF (#10) | `distributorOff_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_OFF_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_DIST_ON_PASSWORD`, `AC_DIST_OFF_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12) dengan unit Available dan unit In Use, serta Subject pending di Approvals (data Pre-setup TC).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Distributor Toggle ON: TC-AC-ACTS-122

1. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
2. Verifikasi `[Add Stock]` row action Stock List: Show (dalam scope)
3. Verifikasi Row action `Detail` / Detail SKU: Show (dalam scope)
4. Verifikasi Download: Show (dalam scope)
5. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
6. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Show (dalam scope)
7. Klik (⋯) pada baris unit di Tab Available
8. Verifikasi `[Delete]` row action Tab Available: Show (dalam scope)
9. Verifikasi Row action `TAG Log` Tab Available: Show (dalam scope)
10. Klik tab `In Use`, lalu klik (⋯) pada baris unit
11. Verifikasi Row action `TAG Log` Tab In Use: Show (dalam scope)
12. Klik tab `Available`, lalu klik `[Event Log]`
13. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show (dalam scope)
14. Tutup modal Event Log
15. Verifikasi Menu Approvals > TAG Stock: Hidden
16. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Hidden
17. Verifikasi Row action `Review` Tab Active: Hidden
18. Verifikasi Row action `Detail` Tab History: Hidden

### Distributor Toggle OFF: TC-AC-ACTS-123

19. Ganti akun: Logout, lalu login sebagai Distributor Toggle OFF (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
20. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
21. Verifikasi `[Add Stock]` row action Stock List: Hidden
22. Verifikasi Row action `Detail` / Detail SKU: Show (dalam scope)
23. Verifikasi Download: Show (dalam scope)
24. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
25. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Show (dalam scope)
26. Klik (⋯) pada baris unit di Tab Available
27. Verifikasi `[Delete]` row action Tab Available: Show (dalam scope)
28. Verifikasi Row action `TAG Log` Tab Available: Show (dalam scope)
29. Klik tab `In Use`, lalu klik (⋯) pada baris unit
30. Verifikasi Row action `TAG Log` Tab In Use: Show (dalam scope)
31. Klik tab `Available`, lalu klik `[Event Log]`
32. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show (dalam scope)
33. Tutup modal Event Log
34. Verifikasi Menu Approvals > TAG Stock: Hidden
35. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Hidden
36. Verifikasi Row action `Review` Tab Active: Hidden
37. Verifikasi Row action `Detail` Tab History: Hidden

## Notes

- Sekitar 35 langkah (di atas smell, 37 langkah): semua blok satu kelas (Role Matrix visibilitas) dengan dataset yang sama; setiap role wajib memuat sebelas Verifikasi (S-01) ditambah langkah navigasi menuju elemen, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30); langkah tiap role identik tetapi hasil Show dan Hidden berbeda.
- Langkah penghubung (S-03): menutup modal Event Log, menutup Detail Approval, dan membuka tab `Available` kembali sebelum langkah berikutnya; Row action `Review` dan `Detail` Tab History hanya diamati bila menu Approvals > TAG Stock tampil, sedangkan Hidden pada menu itu berarti `[Submit]`, `Review`, dan `Detail` tidak dapat dijangkau (Table Tools dan halaman termuat menjadi anchor permukaan, 8b butir 2).
- Temuan untuk QA (S-15): TC sumber menulis Expected `Show (dalam scope)` untuk Distributor tanpa menyebut batas scope yang diasersi; spec mengasersi tampil untuk unit milik sendiri. Sebagian elemen Hidden (e, f, g) diasersi tanpa halaman karena menu Approvals Hidden; TC tidak memberi langkah observasi lain.
- TC-AC-ACTS-123: toggle OFF hanya menyembunyikan `[Add Stock]`; Audit dan Delete atas stok yang ada tetap tersedia. Toggle Local Registration kedua akun diatur oleh Principal di luar spec ini (state awal akun uji; tidak diubah spec).
