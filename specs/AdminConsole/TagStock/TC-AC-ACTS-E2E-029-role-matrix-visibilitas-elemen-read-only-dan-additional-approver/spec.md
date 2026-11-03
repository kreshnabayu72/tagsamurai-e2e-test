---
id: TC-AC-ACTS-E2E-029-role-matrix-visibilitas-elemen-read-only-dan-additional-approver
title: "Role Matrix: Visibilitas Elemen TAG > Stock oleh Read Only dan Additional Approver Tanpa Capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-116
  - TC-AC-ACTS-117
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen TAG > Stock oleh Read Only dan Additional Approver Tanpa Capability

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Read Only`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Read Only (#3) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |
| 2 | Additional Approver tanpa capability Manage TAG stock (#4) | `additionalApprover_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_AA_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_AA_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12) dengan unit Available dan unit In Use, serta Subject pending di Approvals (data Pre-setup TC).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Read Only: TC-AC-ACTS-116

1. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
2. Verifikasi `[Add Stock]` row action Stock List: Hidden
3. Verifikasi Row action `Detail` / Detail SKU: Show
4. Verifikasi Download: Show
5. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
6. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Hidden
7. Klik (⋯) pada baris unit di Tab Available
8. Verifikasi `[Delete]` row action Tab Available: Hidden
9. Verifikasi Row action `TAG Log` Tab Available: Show
10. Klik tab `In Use`, lalu klik (⋯) pada baris unit
11. Verifikasi Row action `TAG Log` Tab In Use: Show
12. Klik tab `Available`, lalu klik `[Event Log]`
13. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show
14. Tutup modal Event Log
15. Klik menu sidebar Approvals > TAG Stock
16. Verifikasi Menu Approvals > TAG Stock: Show
17. Verifikasi Row action `Review` Tab Active: Show
18. Klik `Review` pada Subject pending di Tab Active
19. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Hidden
20. Tutup Detail Approval, lalu klik Tab History
21. Verifikasi Row action `Detail` Tab History: Show

### Additional Approver tanpa capability: TC-AC-ACTS-117

22. Ganti akun: Logout, lalu login sebagai Additional Approver tanpa capability Manage TAG stock (email dan password dari tabel «Role yang diuji»), lalu buka Approvals > TAG Stock
23. Klik menu sidebar Approvals > TAG Stock
24. Verifikasi Menu Approvals > TAG Stock: Show
25. Verifikasi Row action `Review` Tab Active: Show
26. Klik `Review` pada Subject pending di Tab Active
27. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Show
28. Tutup Detail Approval, lalu klik Tab History
29. Verifikasi Row action `Detail` Tab History: Show
30. Verifikasi `[Add Stock]` row action Stock List: Hidden
31. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Hidden
32. Verifikasi `[Delete]` row action Tab Available: Hidden
33. Verifikasi Row action `Detail` / Detail SKU: Hidden
34. Verifikasi Download: Hidden
35. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Hidden
36. Verifikasi Row action `TAG Log` (Tab Available dan Tab In Use): Hidden

## Notes

- Sekitar 35 langkah (di atas smell, 36 langkah): semua blok satu kelas (Role Matrix visibilitas) dengan dataset yang sama; setiap role wajib memuat sebelas Verifikasi (S-01) ditambah langkah navigasi menuju elemen, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30); langkah tiap role identik tetapi hasil Show dan Hidden berbeda.
- Langkah penghubung (S-03): menutup modal Event Log, menutup Detail Approval, dan membuka tab `Available` kembali sebelum langkah berikutnya; Row action `Review` dan `Detail` Tab History hanya diamati bila menu Approvals > TAG Stock tampil, sedangkan Hidden pada menu itu berarti `[Submit]`, `Review`, dan `Detail` tidak dapat dijangkau (Table Tools dan halaman termuat menjadi anchor permukaan, 8b butir 2).
- Temuan untuk QA (S-15): TC sumber menulis Expected `Show (dalam scope)` untuk Distributor tanpa menyebut batas scope yang diasersi; spec mengasersi tampil untuk unit milik sendiri. Sebagian elemen Hidden (e, f, g) diasersi tanpa halaman karena menu Approvals Hidden; TC tidak memberi langkah observasi lain.
- Blok Additional Approver: menu TAG > Stock sendiri tidak tampil karena tanpa capability (Data Uji TC-AC-ACTS-117); elemen Stock List dan Detail SKU (a, b, c, h, i, j, k) diasersi Hidden tanpa halaman, dengan menu Approvals > TAG Stock yang termuat sebagai anchor permukaan.
