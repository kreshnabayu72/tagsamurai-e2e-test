---
id: TC-GS-BRAND-E2E-046-format-tanggal-general-settings
title: "Format Tanggal dan Waktu General Settings pada Tabel Brand, Filter, dan Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-10
  - TC-GS-BRAND-223
  - TC-GS-BRAND-224
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings pada Tabel Brand, Filter, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment, spec ini tidak membuat atau mengubah data brand): 12 brand Client A, termasuk Orion Tech; Modal Changelog Brand memiliki entri.
- State global yang diubah: Date Format dan Time Format General Settings. Nilai awal dibaca lewat API di hook `before`, lalu dipulihkan lewat API di hook `after` yang tetap jalan walau spec gagal di tengah.
- Pengaturan format dilakukan di langkah spec lewat API General Settings.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: pembacaan dan pengubahan General Settings (Date Format dan Time Format) lewat API; memilih tanggal di date picker.

## Test Steps

1. Atur General Settings: Date Format `dd MMM yy` dan Time Format `HH:mm`
2. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-10: Format Last Updated mengikuti General Settings

3. Search `Orion Tech`, tekan Enter
4. Perhatikan sel Last Updated baris Orion Tech
5. Verifikasi Last Updated Orion Tech tampil dengan pola `dd MMM yy HH:mm`
6. Hapus keyword Search, tekan Enter
7. Verifikasi tidak ada sel Last Updated bernilai `—` pada tabel

### TC-GS-BRAND-223: Date/Time Format General Settings di tabel utama dan filter

8. Atur General Settings: Date Format `DDD, MMM dd, yyyy` dan Time Format `hh:mm a`
9. Muat ulang halaman Brand
10. Perhatikan kolom Last Updated
11. Verifikasi Last Updated tampil dengan pola `DDD, MMM dd, yyyy hh:mm a`
12. Buka Filter, lalu pilih tanggal di Filter Last Updated
13. Verifikasi input Filter Last Updated menampilkan pola `DDD, MMM dd, yyyy`

### TC-GS-BRAND-224: Date/Time Format General Settings di Modal Changelog

14. Buka Changelog
15. Verifikasi kolom Date Modal Changelog tampil dengan pola `DDD, MMM dd, yyyy hh:mm a`
16. Pilih tanggal di Filter Date
17. Verifikasi input Filter Date menampilkan pola `DDD, MMM dd, yyyy`
18. Tutup Modal Changelog
19. Pulihkan Date Format dan Time Format General Settings ke nilai awal yang dibaca di hook `before`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: format `dd MMM yy` / `HH:mm` (TC-GS-BRAND-10) lebih dulu, lalu satu kali ganti format ke `DDD, MMM dd, yyyy` / `hh:mm a` untuk TC-GS-BRAND-223 dan TC-GS-BRAND-224 yang memakai precondition format yang sama, sehingga format hanya diganti dua kali.
- Langkah penghubung: langkah 3 (Search Orion Tech untuk menemukan baris), langkah 6 (menghapus keyword Search), langkah 9 (muat ulang halaman agar format baru dimuat), langkah 18 (menutup Modal Changelog), dan langkah 19 (memulihkan General Settings; hook `after` sebagai cadangan).
- Spec ini mengubah state global (General Settings) sehingga tidak boleh paralel dengan spec lain di suite; suite memang `parallel: false`.
