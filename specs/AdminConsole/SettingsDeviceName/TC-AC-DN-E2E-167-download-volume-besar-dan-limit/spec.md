---
id: TC-AC-DN-E2E-167-download-volume-besar-dan-limit
title: "Download di Atas 5.000 Baris (List dan Changelog) dan Create Tidak Ikut Master Data Count Limit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-607
  - TC-AC-DN-608
  - TC-AC-DN-605
coverage:
  web: automated
---

# Download di Atas 5.000 Baris (List dan Changelog) dan Create Tidak Ikut Master Data Count Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal Uji Download Besar, Pre-setup #26 `totalControlBig_automated_{namaCompany}@qwertysystem.net`; email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password `Spectra.env.AC_DN_BIG_PASSWORD` (disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (`Spectra.env.AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca kecuali dinyatakan): #26 Principal `Principal Uji Download Besar` (5.001 Device Name `Bulk Device 0001` dan seterusnya, 5.001 entri Changelog hasil seed); #25 Principal `Principal Uji Volume` (1000 Device Name, Master Data Count Limit 1000).
- Data Dinamis: `Device Ke 1001 {runId}-167` (`Unit`, `Accessory`) dibuat lewat form Create pada Principal Uji Volume (TC-AC-DN-605) dan dihapus lewat API di hook `after` sehingga jumlah kembali 1000.
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- Akun lain (ganti akun eksplisit di langkah, disediakan tim FE): Pre-setup #25 `totalControlVolume_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DN_VOLUME_PASSWORD`.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas CSV; kemampuan baca jumlah Device Name Principal Uji Volume; seed Principal Uji Download Besar dan Principal Uji Volume. Kelas harness e: volume 5.001 baris.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-607: Download List di atas 5.000 baris memakai loading screen lalu berkas terunduh otomatis
2. Klik ikon Download lalu klik `Download as CSV`
3. Verifikasi loading screen tampil
4. Verifikasi tidak ada toast "Preparing your export. We'll notify you when it's ready."
5. Verifikasi tidak ada notifikasi in-app
6. Verifikasi tidak berpindah ke halaman Export History (halaman Device Name tetap tampil)
7. Tunggu sampai berkas siap
8. Verifikasi file `Device-Name.csv` terunduh otomatis tanpa klik tambahan
9. Verifikasi tidak ada toast sukses
10. Buka file hasil unduhan dengan pembaca berkas CSV
11. Verifikasi file memuat satu baris header ditambah 5.001 baris data
12. TC-AC-DN-608: Download Changelog di atas 5.000 baris memakai loading screen lalu berkas terunduh otomatis
13. Klik ikon Changelog di toolbar
14. Verifikasi popup `Changelog: Device Name` tampil
15. Klik ikon Download di toolbar popup lalu klik "Download as CSV"
16. Verifikasi loading screen tampil
17. Verifikasi tidak ada toast "Preparing your export. We'll notify you when it's ready."
18. Verifikasi tidak ada notifikasi in-app
19. Verifikasi tidak berpindah ke halaman Export History (popup Changelog tetap tampil)
20. Tunggu sampai berkas siap
21. Verifikasi file `Changelog-Device-Name.csv` terunduh otomatis tanpa klik tambahan
22. Verifikasi tidak ada toast sukses
23. Buka file hasil unduhan dengan pembaca berkas CSV
24. Verifikasi file memuat satu baris header ditambah 5.001 baris data
25. Klik ikon close `(X)` pada popup Changelog
26. TC-AC-DN-605: Create Device Name tidak ikut Master Data Count Limit
27. Logout dari akun Total Control Principal Uji Download Besar
28. Login sebagai Total Control Principal Uji Volume (`Fixture.settings-device-name.akunVolume`, password dari `Spectra.env.AC_DN_VOLUME_PASSWORD`)
29. Klik `+ Device Name`
30. Ketik "Device Ke 1001 {runId}-167" pada field Device Name
31. Pilih "Unit" pada field Measurement
32. Pilih Category `Accessory` (expand `TAG` lalu `NFC`)
33. Klik `[Submit]`
34. Verifikasi toast sukses "Success, device name has been created."
35. Verifikasi tidak ada dialog blok limit dan popup form tertutup
36. Ketik Search `Device Ke 1001 {runId}-167`, tekan Enter
37. Verifikasi baris `Device Ke 1001 {runId}-167` tampil sebagai Device Name ke-1001 (jumlah Device Name Principal Uji Volume menjadi 1001 dari baseline 1000)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): ganti akun eksplisit (logout lalu login) sebelum TC-AC-DN-605; menutup popup Changelog sebelum ganti akun.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: mengikuti sourceTc.
- Ukuran spec (37 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3).
- Temuan untuk QA:
  - TC-AC-DN-605 menyebut Post Condition jumlah 1001 tanpa langkah observasi; spec mengasersi 'ke-1001' sebagai Expected c lewat kemampuan baca jumlah Device Name (disediakan tim FE/BE).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
