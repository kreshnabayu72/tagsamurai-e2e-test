---
id: TC-GS-DIV-E2E-044-tabel-utama-mutasi-realtime-create-dan-edit
title: "Refleksi Real-time Hasil Create dan Edit Terhadap Kriteria Search/Filter Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-70
  - TC-GS-DIV-71
coverage:
  web: automated
---

# Refleksi Real-time Hasil Create dan Edit Terhadap Kriteria Search/Filter Aktif

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Aktifkan search keyword 'Finance'
3. Verifikasi hanya data yang mengandung 'Finance' yang tampil di tabel
4. Buka modal Create Division lalu buat divisi baru bernama 'Technology'
5. Verifikasi divisi baru 'Technology' berhasil dibuat namun TIDAK muncul di tabel yang sedang terfilter 'Finance'
6. Hapus filter search 'Finance'
7. Verifikasi divisi 'Technology' kini terlihat pada daftar tabel
8. Buka modal Edit pada divisi 'Technology', ubah namanya menjadi 'Finance Tech'
9. Terapkan kembali filter search 'Finance'
10. Verifikasi record 'Finance Tech' kini ikut tampil pada hasil pencarian secara konsisten

## Notes

- Memastikan konsistensi tampilan mutasi data terhadap kondisi filter aktif (division.md §9.7).
