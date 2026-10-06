---
id: TC-AC-SU-E2E-043-accessibility-dan-plan-gating-cross-cutting
title: "Aksesibilitas tooltip alasan disabled, keyboard navigation, aria-live polite, dan verifikasi ketiadaan plan gating"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-196
  - TC-AC-SU-197
  - TC-AC-SU-198
  - TC-AC-SU-202
  - TC-AC-SU-203
coverage:
  web: automated
---

# Aksesibilitas tooltip alasan disabled, keyboard navigation, aria-live polite, dan verifikasi ketiadaan plan gating

## Prerequisites

- Login sebagai Role: Principal Total Control
- Halaman User List dan Detail User dengan berbagai elemen interaktif

## Test Steps

### Verifikasi Aksesibilitas Tooltip dan Keyboard

1. Arahkan kursor pada setiap elemen yang berstatus Disabled di halaman User List dan Detail User
2. Verifikasi seluruh elemen disabled memunculkan tooltip 🔖 dengan alasan kontekstual spesifik
3. Navigasikan halaman User List menggunakan tombol `Tab` dan `Enter` pada keyboard
4. Verifikasi fokus visual berpindah secara logis dan tombol `Enter` mengaktifkan switch atau membuka modal
5. Picukan toast notifikasi atau pesan error validasi, inspeksi elemen DOM
6. Verifikasi elemen notifikasi memuat atribut `aria-live="polite"` untuk screen reader

### Verifikasi Ketiadaan Plan Gating dan Batas Kuota User

1. Buka seluruh menu dan fitur pada Admin Console > Settings > User
2. Verifikasi tidak ada banner upsell, limitasi tier langganan klien, atau gating paket berbayar (Admin Console adalah produk internal)
3. Verifikasi tidak ada batas Master Data Count Limit untuk jumlah pengguna

## Notes

- Admin Console dirancang dengan standar aksesibilitas inklusif tanpa batasan kuota internal.
