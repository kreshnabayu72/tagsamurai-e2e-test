---
id: TC-GS-POS-E2E-031-download-dan-independensi-cache
title: Download — Semua Data vs Ter-filter; Independensi Cache Persistensi Tabel
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-31
  - TC-GS-POS-119
coverage:
  web: automated
---

# Download — Semua Data vs Ter-filter; Independensi Cache Persistensi Tabel

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia filter Last Updated dan search untuk membedakan kondisi ter-filter vs all data.
- Konfigurasi kolom pernah dikustomisasi (Visibility/Reorder/Pin) untuk menguji persistensi.
- Download tersedia (CSV/XLSX). Tidak ada toast sukses saat download (sesuai TC-GS-POS-73).

## Test Steps

### A. Download sukses (semua data)

1. Hapus semua filter/search agar dalam kondisi semua data.
2. Klik icon Download pada toolbar.
3. Pilih CSV (atau XLSX) dan unduh.
4. Verifikasi file terunduh dengan filename `"Position"`.
5. Verifikasi isi file sesuai seluruh data yang tampil (all data), tanpa pembatasan filter.
6. Verifikasi **tidak ada toast sukses** setelah unduhan.

### B. Download dengan filter aktif

7. Terapkan filter Last Updated (range) atau kombinasi filter+search sehingga data ter-filter.
8. Verifikasi tabel menampilkan data ter-filter.
9. Klik icon Download.
10. Pilih CSV/XLSX dan unduh.
11. Verifikasi file terunduh dengan filename `"Position"`.
12. Verifikasi isi file sesuai kondisi ter-filter (hanya baris yang match kriteria aktif), bukan all data.
13. Verifikasi **tidak ada toast sukses** setelah unduhan.

### C. Independensi cache persistensi tabel utama

14. Kustomisasi konfigurasi kolom tabel utama (mis. sembunyikan kolom Last Updated, atau pindah/ubah pin) via Overlay Column Visibility/Setup Column (mengacu ke 033–034).
15. Logout dari aplikasi.
16. Login kembali sebagai user yang sama.
17. Buka halaman `Global Settings > User > Position`.
18. Verifikasi setting Column Visibility & Pin tabel utama tetap utuh (survive session/logout).
19. Verifikasi tidak ter-reset ke konfigurasi pabrik.

## Notes

- Perbedaan isi file antara A dan B membuktikan download menghormati state filter/search saat ini.
- C menegaskan persistensi terpisah (localStorage/session sesuai platform) dan independen dari state filter/search.
