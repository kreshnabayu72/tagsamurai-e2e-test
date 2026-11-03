---
id: TC-AC-DN-E2E-121-state-preservation-refresh
title: "State List: Refresh F5 Mempertahankan Search, Sort, Filter, Halaman, dan Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-381
  - TC-AC-DN-382
  - TC-AC-DN-383
  - TC-AC-DN-384
coverage:
  web: automated
---

# State List: Refresh F5 Mempertahankan Search, Sort, Filter, Halaman, dan Page Size

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #15 Brand `Brand A`; #16 Device Name inti beserta SKU-nya (`Gate Antenna`, `NFC Tag`, `RFID Reader` ber-Brand A); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified (`Tag Reel` 15/09/26 10:10 sebagai Newest First); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Search, Filter, Sort, halaman, dan page size dikembalikan ke awal di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-381: Refresh F5 mempertahankan keyword Search

1. Ketik Search `rfid`, tekan Enter
2. Muat ulang halaman dengan F5
3. Verifikasi kolom pencarian masih berisi `rfid`
4. Verifikasi tabel menampilkan 1 baris: RFID Reader
5. Klik `(←)` pada kotak Search

### TC-AC-DN-382: Refresh F5 mempertahankan kolom dan arah sort

6. Klik header `Last Modified` dua kali (Newest First)
7. Muat ulang halaman dengan F5
8. Verifikasi header `Last Modified` tetap menampilkan panah turun
9. Verifikasi urutan tetap Newest First
10. Klik header `Last Modified` ketiga kali (netral)

### TC-AC-DN-383: Refresh F5 mempertahankan Filter ter-Apply

11. Klik ikon Filter, klik field `Brand`, centang `Brand A`, lalu klik `[Apply]`
12. Muat ulang halaman dengan F5
13. Verifikasi tabel tetap menampilkan 3 baris: Gate Antenna, NFC Tag, RFID Reader
14. Klik ikon Filter
15. Verifikasi Filter Panel menampilkan chip `Brand A`
16. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-384: Refresh F5 mempertahankan halaman aktif dan page size

17. Pilih page size `25`
18. Klik tombol halaman berikutnya dua kali
19. Muat ulang halaman dengan F5
20. Verifikasi tabel tetap di halaman 3 dengan page size 25 (bukan reset ke halaman 1)
21. Pilih page size `10`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 5, 10, 16, dan 21 mengembalikan Search, sort, Filter, dan page size ke awal.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - Persistensi state List setelah F5 tidak disebut sebagai penyimpanan lokal atau URL di TC; spec tidak menyebut mekanismenya (S-13).
