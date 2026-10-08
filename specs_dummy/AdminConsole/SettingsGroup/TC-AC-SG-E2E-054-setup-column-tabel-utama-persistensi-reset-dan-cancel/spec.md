---
id: TC-AC-SG-E2E-054-setup-column-tabel-utama-persistensi-reset-dan-cancel
title: "Setup Column tabel utama: persistensi reload F5, Reset to Default, Cancel Discard, dan isolasi cache antar tabel"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-209
  - TC-AC-SG-210
  - TC-AC-SG-211
  - TC-AC-SG-212
coverage:
  web: automated
---

# Setup Column tabel utama: persistensi reload F5, Reset to Default, Cancel Discard, dan isolasi cache antar tabel

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

### Persistensi Konfigurasi Reload (F5)
1. Ubah konfigurasi Setup Column (sembunyikan 1 kolom) lalu klik `[Save]`
2. Lakukan reload halaman browser (F5)
3. Verifikasi susunan dan visibilitas kolom tabel utama tetap bertahan sesuai konfigurasi terakhir
### Reset to Default
4. Buka kembali Setup Column lalu klik tombol `[Reset to Default]` di footer
5. Verifikasi seluruh checkbox dan urutan kolom kembali ke kondisi bawaan di Live Preview
6. Klik `[Save]` dan verifikasi tabel utama pulih ke susunan default
### Discard Perubahan saat Cancel
7. Buka Setup Column, ubah beberapa checkbox, lalu klik `[Cancel]` (atau icon `[✕]`)
8. Verifikasi modal tertutup dan perubahan dibatalkan tanpa tersimpan di tabel
### Isolasi Cache Antar Tabel
9. Buka Modal Changelog lalu buka Setup Column-nya
10. Verifikasi konfigurasi kolom Changelog tidak terpengaruh oleh konfigurasi tabel utama (cache terisolasi per tabel)

## Notes

- Cache Setup Column disimpan per tabel dan terisolasi mandiri.
