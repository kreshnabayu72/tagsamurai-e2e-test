---
id: TC-AC-DN-E2E-178-all-tags-self-purchased-dan-registri
title: "All TAGs: Pemilih Device Name Self-Purchased Template dan Registri Tag Jalur A/B setelah Rename"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-657
  - TC-AC-DN-661
coverage:
  web: automated
---

# All TAGs: Pemilih Device Name Self-Purchased Template dan Registri Tag Jalur A/B setelah Rename

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun konteks kedua: Total Control pada entitas Client `Client Jaringan` `totalControlClient_automated_{namaCompany}@qwertysystem.net` (Pre-setup #11; email lewat `Fixture.settings-device-name.akunClient`), password `Spectra.env.AC_DN_CLIENT_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Konteks Client dibuka dan login di langkah spec dan ditutup di akhir tiap blok TC.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #11, kode tag Jalur A (`tagJalurA`) dan Jalur B (`tagJalurB`) yang di-seed. Nama dinamis dibentuk `<nama dasar> {runId}-178` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Meter`, `Unit`; #14 Pohon Category (`TAG` > `NFC` > `Tag`); #16 `Door Antenna` (Antenna, di luar konteks `NFC`); #27 pola data khusus TC-AC-DN-661; #29 Client Jalur B siap aktivasi (toggle Self-Purchased aktif, kuota `NFC` tersedia).
- Data Dinamis (milik spec; dibuat fixture BE di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name, SKU, tag NFC, dan sesi Activate di Event Log disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Data | Detail | Dipakai oleh |
  |---|---|---|---|
  | R1 | Device Name `Reel Pilih {runId}-178` | Measurement `Meter`, Category `TAG > NFC > Tag`, tanpa SKU | TC-AC-DN-657 |
  | R2 | Device Name `NFC Registri {runId}-178` | Measurement `Unit`, Category `TAG > NFC > Tag`, SKU `NR-A-N1-{runId}-178` (Brand A/Model N1) | TC-AC-DN-661 |
  | T1 | Tag NFC Jalur A milik Client | stok resmi, SKU di bawah R2 | TC-AC-DN-661 |
  | T2 | Tag NFC Jalur B (Self-Purchased) milik Client | menyimpan ID Device Name R2 | TC-AC-DN-661 |
  | E1 | Sesi Activate di Event Log Client | memuat T1; nama Device Name R2 sebelum rename tersimpan sebagai snapshot | TC-AC-DN-661 |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_CLIENT_PASSWORD`.

## Test Steps

### TC-AC-DN-657: Rename mengganti nama opsi pada pemilih Self-Purchased Template All TAGs

1. Sebagai Principal, ketik Search `Reel Pilih {runId}-178`, tekan Enter
2. Buka menu aksi pada baris `Reel Pilih {runId}-178`, klik `Edit`
3. Kosongkan field Device Name lalu ketik "Reel Pilih Pro {runId}-178"
4. Klik `[Save]`
5. Verifikasi toast sukses "Success, device name has been updated."
6. Buka konteks browser Client, login sebagai Client (`Spectra.env.AC_DN_CLIENT_PASSWORD`)
7. Buka halaman `Global Settings > TAG`, klik `[+ Activate TAG]`, pilih `NFC`, konfirmasi popup pengantar
8. Buka section `Self-Purchased Template`, klik field `Device Name`
9. Verifikasi daftar opsi `Device Name` memuat "Reel Pilih Pro {runId}-178"
10. Verifikasi daftar opsi `Device Name` tidak memuat "Reel Pilih {runId}-178"
11. Verifikasi daftar opsi `Device Name` tidak memuat "Door Antenna"
12. Tutup halaman Activate TAG tanpa Submit
13. Tutup konteks browser Client

### TC-AC-DN-661: Rename tercermin pada registri All TAGs, Event Log tetap snapshot

14. Buka konteks browser Client, login sebagai Client (`Spectra.env.AC_DN_CLIENT_PASSWORD`)
15. Buka halaman `Global Settings > TAG`, Tab All
16. Verifikasi kolom Device Name tag Jalur A menampilkan `NFC Registri {runId}-178`
17. Verifikasi kolom Device Name tag Jalur B menampilkan `NFC Registri {runId}-178`
18. Sebagai Principal, ketik Search `NFC Registri {runId}-178`, tekan Enter
19. Buka menu aksi pada baris `NFC Registri {runId}-178`, klik `Edit`
20. Kosongkan field Device Name lalu ketik "NFC Registri Pro {runId}-178"
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, device name has been updated."
23. Sebagai Client, muat ulang halaman `Global Settings > TAG`, Tab All
24. Verifikasi kolom Device Name tag Jalur A menampilkan `NFC Registri Pro {runId}-178`
25. Verifikasi kolom Device Name tag Jalur B menampilkan `NFC Registri Pro {runId}-178`
26. Verifikasi registri tidak lagi menampilkan `NFC Registri {runId}-178` pada kedua tag
27. Verifikasi SKU tag Jalur A tetap `NR-A-N1-{runId}-178`, Brand tetap `Brand A`, dan Model/Type tetap `Model N1`
28. Buka Detail aktivasi sesi Activate yang memuat tag Jalur A di Event Log
29. Verifikasi Detail aktivasi menampilkan Device Name `NFC Registri {runId}-178` (snapshot)
30. Tutup konteks browser Client

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 dan 18 (Search) menemukan baris record milik spec; langkah 12, 13, 30 menutup halaman Activate TAG dan konteks Client (S-09). Konteks Client dibuka per blok karena TC-AC-DN-661 butuh sesi bersih.
- Record milik spec (S-06, S-12): R1 menggantikan `Tag Reel` dan R2 beserta T1, T2, E1 menggantikan `NFC Tag` Pre-setup #16 dan #27 TC sumber; Pre-setup #16 tidak diubah, jadi pemulihan nama oleh baseline TC tidak diperlukan. Nama yang dicari absence bukan substring nama hasil rename (R-13): "Reel Pilih {runId}-178" dan "Reel Pilih Pro {runId}-178" tidak saling memuat; langkah 9 menjadi anchor positif langkah 10 dan 11 (8b butir 2). Langkah 26 didahului langkah 24 dan 25.
- Urutan: mengikuti sourceTc. Langkah 16 dan 17 (Expected a TC-AC-DN-661) mendahului rename karena keadaan sebelum rename harus teramati (8b butir 5).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-657 dan TC-AC-DN-661 (pemulihan nama).
  - TC-AC-DN-661 langkah 5: letak Event Log dan cara membuka Detail aktivasi tidak dinyatakan TC; langkah 28 mengikuti teks TC. Label tombol popup pengantar `[+ Activate TAG]` tidak dirinci TC; langkah 7 mengikuti teks TC.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-178` (S-12).
