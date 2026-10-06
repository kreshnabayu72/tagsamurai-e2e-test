---
id: TC-GS-GSET-E2E-028-setup-column-screening-dan-popup
title: "Setup Column: screening overlay dan live preview"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-81
  - TC-GS-GSET-82
coverage:
  web: automated
---

# Setup Column: overlay, popup, dan live preview

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Modal Changelog memiliki data sehingga kolom dapat diperiksa.

## Test Steps

### Overlay dan popup

1. Buka Modal Changelog
2. Klik header kolom `(⋯)`/Column Visibility pada header tabel
3. Verifikasi Quick Panel/overlay terbuka menampilkan keenam kolom data (`Date`, `Action`, `Field`,
   `Old Value`, `New Value`, `Modified By`) dengan checkbox ☑ Hideable yang ter-centang & aktif serta
   drag handle aktif
4. Klik untuk membuka Popup Modal Setup Column
5. Verifikasi popup menampilkan header title `Setup Column` + tombol `[✕]`
6. Verifikasi body popup menampilkan 6 baris kolom + live preview tabel
7. Verifikasi footer popup menampilkan `[Reset to Default]`, `[Cancel]`, dan `[Save]`
8. Verifikasi popup memiliki z-index di depan dialog changelog induk (popup di atas)

### Popup sebagai kombinasi urutan/pin/hide + live preview

9. Verifikasi pada tiap baris popup tersedia kontrol untuk: (a) drag handle urutan,
   (b) pin/unpin, dan (c) toggle hide/unhide
10. Verifikasi perubahan yang dilakukan pada popup langsung tercermin pada tabel di belakangnya
    (live preview) bahkan sebelum `[Save]`

### Tutup popup & persist

11. Pindahkan kolom `Date` dan sembunyikan kolom `New Value` lewat popup
12. Klik `[Save]` untuk menyimpan konfigurasi
13. Verifikasi tabel menampilkan hasil yang terpilih (kolom tersembunyi dan urutan baru)
14. Muat ulang halaman
15. Verifikasi preferensi urutan/hidden tetap bertahan setelah muat ulang (persist di local storage)

## Notes

- Kolom `Actions (⋯)` pemicu Setup Column tidak terdaftar di checklist manapun dan selalu rightmost —
  dibuktikan khusus di spec 032 (TC-GS-GSET-157). Teknis hide/unhide, drag, dan pin diuji terpisah
  (spec 029, 030, 031); spec ini membuktikan struktur popup dan live preview yang menyatukannya.