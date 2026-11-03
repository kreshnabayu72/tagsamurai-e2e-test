---
id: TC-AC-DN-E2E-003-kolom-category-badge
title: "Kolom Category: Urutan Default, Badge, Hover Jalur Penuh, Pemotongan 25 Karakter, Fokus Keyboard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-9
  - TC-AC-DN-10
  - TC-AC-DN-11
  - TC-AC-DN-12
  - TC-AC-DN-597
coverage:
  web: automated
---

# Kolom Category: Urutan Default, Badge, Hover Jalur Penuh, Pemotongan 25 Karakter, Fokus Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Device Name inti (#16: `Cable Tester`, `Door Antenna`, `Legacy Scanner`, `NFC Tag`, `Gate Antenna`, `Barcode Station`), seed 120 Device Name (#17), dan Device Name panjang (#23); seluruhnya baca-saja. Tidak ada data Dinamis.

## Test Steps

### TC-AC-DN-9: Urutan default List: Device Name A-Z tanpa membedakan huruf besar-kecil

1. Verifikasi urutan baris halaman 1: Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
2. Verifikasi tidak ada indikator panah sort aktif pada header kolom (kondisi netral = urutan bawaan Device Name A-Z)

### TC-AC-DN-10: Kolom Category menampilkan satu badge Primary berisi nama Category

3. Verifikasi Cable Tester: satu badge Primary `Accessory`
4. Verifikasi Door Antenna: satu badge Primary `Antenna`
5. Verifikasi Legacy Scanner: satu badge Primary `UHF Handheld`
6. Verifikasi NFC Tag: satu badge Primary `Tag`
7. Verifikasi tiap sel Category pada baris `Cable Tester`, `Door Antenna`, `Legacy Scanner`, dan `NFC Tag` hanya berisi satu badge
8. Verifikasi tiap sel itu tidak menampilkan nama parent (mis. `Hardware`, `Handheld Reader`, `TAG`, `NFC`)

### TC-AC-DN-11: Hover badge Category menampilkan jalur penuh dari root

9. Hover badge Category pada baris `Legacy Scanner`
10. Verifikasi tooltip `Hardware > Handheld Reader > UHF Handheld`
11. Hover badge Category pada baris `Gate Antenna`
12. Verifikasi tooltip `Hardware > Smart Fixed Reader > Antenna`

### TC-AC-DN-12: Badge Category lebih dari 25 karakter dipotong 12 huruf pertama, dua titik, 12 huruf terakhir

13. Verifikasi baris `Barcode Station`: badge `Perangkat Pe..ang Industri`
14. Hover badge Category pada baris `Barcode Station`
15. Verifikasi baris `Barcode Station`: tooltip jalur penuh `TAG > NFC > Perangkat Pemindai Kode Batang Industri`
16. Verifikasi baris `Legacy Scanner` (12 karakter): badge `UHF Handheld` tampil penuh tanpa pemotongan

### TC-AC-DN-597: Badge Category terpotong menampilkan jalur penuh saat menerima fokus keyboard

17. Tekan Tab sampai fokus berada pada badge Category baris `Barcode Station`
18. Verifikasi badge menampilkan 12 huruf pertama, `..`, dan 12 huruf terakhir nama Category (`Perangkat Pe..ang Industri`)
19. Verifikasi tooltip tampil saat fokus keyboard dan memuat jalur Category penuh `TAG > NFC > Perangkat Pemindai Kode Batang Industri`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- TC-AC-DN-9 diletakkan pertama karena mengasersi urutan default sebelum interaksi apa pun; TC-AC-DN-12 dan TC-AC-DN-597 memakai baris `Barcode Station` yang sama.
- TC-AC-DN-12: langkah perhatian pada badge `Legacy Scanner` (12 karakter) ditulis sebagai satu `Verifikasi` tanpa hover karena Expected-nya hanya badge penuh.
- TC-AC-DN-597: nilai badge terpotong pada langkah 18 diambil dari Expected TC-AC-DN-12 (Category yang sama, `Perangkat Pemindai Kode Batang Industri`); Expected TC-AC-DN-597 hanya menyebut aturan 12 huruf pertama, `..`, dan 12 huruf terakhir.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
